from django.contrib import admin
from django.urls import path
from manga.views import MangaDetailListView, GeneralPageView, CommentsView
from users.views import LoginViewSet, RegisterViewSet

create_list = {'get': 'list', 'post': 'create'}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('manga/<int:id>/', MangaDetailListView.as_view({'get': 'retrieve'})),
    path('general_page/', GeneralPageView.as_view({'get': 'list'})),
    path('login/', LoginViewSet.as_view(create_list), name="login"),
    path('register/', RegisterViewSet.as_view(create_list), name='signup'),
    path('comments/', CommentsView.as_view(create_list)),
]

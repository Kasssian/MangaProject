from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from manga.views import MangaDetailListView, GeneralPageView, CommentsView
from users.views import LoginViewSet, RegisterViewSet

create_list = {'get': 'list', 'post': 'post'}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('manga/<int:id>/', MangaDetailListView.as_view({'get': 'retrieve'})),
    path('general_page/', GeneralPageView.as_view({'get': 'list'})),
    path('login/', LoginViewSet.as_view(create_list), name="login"),
    path('register/', RegisterViewSet.as_view(create_list), name='signup'),
    path('comments/', CommentsView.as_view(create_list)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Manga, Comments
from .serializers import GeneralPageSerializer, MangaDetailSerializer, CommentsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from manga.filters import MangaFilters
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 10000


class MangaDetailListView(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Manga.objects.all()
    serializer_class = MangaDetailSerializer


class GeneralPageView(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = GeneralPageSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = (MangaFilters)
    pagination_class = LargeResultsSetPagination


class CommentsView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

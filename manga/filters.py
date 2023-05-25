from django_filters import rest_framework as filters
from manga.models import Manga


class MangaFilters(filters.FilterSet):
    title = filters.CharFilter()
    genre = filters.NumberFilter()
    year = filters.RangeFilter()

    class Meta:
        model = Manga
        fields = ['title', 'genre', 'year']

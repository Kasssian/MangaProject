from rest_framework import serializers
from .models import *


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class MangaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'

    comments = CommentsSerializer(many=True)


class GeneralPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['title', 'year']

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import RegisteredUsers


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Manga(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=(
        ('Манга', 'Манга'),
        ('Комикс', 'Комикс'),
        ('Манхва', 'Манхва'),
    ))
    year = models.IntegerField(validators=[MinValueValidator(1960), MaxValueValidator(2099)])
    genre = models.ManyToManyField(Genre)
    description = models.TextField()

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return self.user

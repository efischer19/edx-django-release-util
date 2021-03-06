from django.db import models


class Author(models.Model):
    class Meta:
        app_label = 'release_util'
        unique_together = ('name', 'slug')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    age = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)


class Book(models.Model):
    class Meta:
        app_label = 'release_util'
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

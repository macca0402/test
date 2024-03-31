from django.db import models
from datetime import timezone


class Author(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.title

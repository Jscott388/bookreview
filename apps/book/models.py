from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk':self.id})

class Review(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)
    rating = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

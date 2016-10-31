from django.forms import ModelForm
# from django.forms.models import inlineformset_factory

from .models import Book, Review

class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'rating']

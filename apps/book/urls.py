from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import BookHomeRedirectView, BookHomeListView, BookDetailView, BookCreateView, BookDeleteView, BookUpdateView, ReviewListView


urlpatterns = [

    url(r'^$', BookHomeListView.as_view(), name="book-home"),
    url(r'^(?P<pk>\d+)/$', BookDetailView.as_view(), name="book-detail"),
    url(r'^create/$', BookCreateView.as_view(), name="book-create"),
    url(r'^delete/(?P<pk>\d+)/$', BookDeleteView.as_view(), name="book-delete"),
    url(r'^update/(?P<pk>\d+)/$', BookUpdateView.as_view(), name="book-update"),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^review/$',  ReviewListView.as_view(), name="review"),

]

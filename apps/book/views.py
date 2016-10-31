from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.views import View
from django.views.generic import FormView, RedirectView, CreateView, ListView, DetailView, DeleteView, UpdateView, FormView
from django.views.generic.detail import SingleObjectMixin

from .models import Book, Review
from .forms import BookForm, ReviewForm

# Create your views here.
class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('book-home')
    template_name = "accounts/login.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class LogoutView(RedirectView):
    url = reverse_lazy('book-home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = "registration/signup.html"


class BookHomeListView(ListView):
    context_object_name = 'books'
    fields = ('title', 'added_by', 'created_at')
    model = Book
    template_name = "book/book_home.html"

class BookHomeRedirectView(RedirectView):
    url = reverse_lazy('book-home')

class BookDisplay(DetailView):
    template_name = "book/book.html"
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookDisplay, self).get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context

class Review(SingleObjectMixin, FormView):
    template_name = 'single_form.html'
    form_class = ReviewForm
    model = Book

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super(Review, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.title_id = self.kwargs.get('pk')
        form.instance.creator = self.request.user
        return super(Review, self).form_valid(form)

    def get_success_url(self):
        return reverse('book-detail', kwargs={'pk': self.object.pk})

class BookDetailView(View):
    def query_set(self):
        return Book.objects.all()

    def get(self, request, *args, **kwargs):
        view = BookDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = Review.as_view()
        return view(request, *args, **kwargs)

class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = "book/book_create.html"
    fields = ('title', 'author')
    model = Book

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(BookCreateView, self).form_valid(form)

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book-home')

class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "book/book_update.html"
    model = Book
    form_class = BookForm

class ReviewListView(ListView):
    template_name = "review.html"
    model = Review

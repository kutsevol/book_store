from django.http import HttpResponseRedirect, Http404
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse

from .forms import BookForm
from .models import Books, AuthorsToBooks, StatusLog


class IndexView(ListView):
    model = Books
    context_object_name = 'books'
    template_name = 'books_list.html'
    order = 'asc'

    def get_ordering(self):
        self.order = self.request.GET.get('order')
        ordering = self.request.GET.get('ordering', 'published_date')
        if self.order == 'desc':
            ordering = '-' + ordering
        return ordering

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['order'] = self.order
        return context


class EditBook(UpdateView):
    model = Books
    form_class = BookForm
    template_name = 'book_edit.html'
    context_object_name = 'books'

    def form_valid(self, form):
        book = form.save(commit=False)

        AuthorsToBooks.objects.filter(book=book).delete()

        for author in form.cleaned_data['authors']:
            authors = AuthorsToBooks()
            authors.book = book
            authors.author = author
            authors.save()

        book.save()

        return HttpResponseRedirect(self.get_success_url())


class AddBook(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'book_add.html'
    context_object_name = 'books'

    def get_success_url(self):
        return reverse('books')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.save()

        for author in form.cleaned_data['authors']:
            authors = AuthorsToBooks()
            authors.book = book
            authors.author = author
            authors.save()

        return HttpResponseRedirect(self.get_success_url())


class DeleteBook(DeleteView):
    model = Books

    def get_success_url(self):
        return reverse('books')


class ViewLogs(ListView):
    model = StatusLog
    context_object_name = 'logs'
    template_name = 'logs_list.html'

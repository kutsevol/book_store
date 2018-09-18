from django.urls import path

from .views import IndexView, EditBook, AddBook, DeleteBook, ViewLogs


urlpatterns = [
    path('', IndexView.as_view(), name='books'),
    path('add/', AddBook.as_view(), name='book_add'),
    path('logs/', ViewLogs.as_view(), name='logs'),
    path('delete/<int:pk>/', DeleteBook.as_view(), name='book_delete'),
    path('edit/<int:pk>/', EditBook.as_view(), name='book_edit'),
]

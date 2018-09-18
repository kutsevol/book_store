from django.urls import path

from .views import IndexView, EditBook, AddBook, ViewLogs


urlpatterns = [
    path('', IndexView.as_view(), name='books'),
    path('edit/<int:pk>/', EditBook.as_view(), name='book_edit'),
    path('add/', AddBook.as_view(), name='book_add'),
    path('logs/', ViewLogs.as_view(), name='logs'),
]

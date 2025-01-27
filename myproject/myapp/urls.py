from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Connects the root URL of this app to the `book_list` view
]

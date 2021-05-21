from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.books),
    path('extra_author/<int:book_id>', views.extra_author),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('authors/<int:author_id>', views.authors_info),
    path('extra_book/<int:author_id>', views.extra_book),
    ]
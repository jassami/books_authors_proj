from django.shortcuts import redirect, render
from .models import *

def index(request):
    context= {
        'all_books': Book.objects.all()
    }
    return render(request, 'index.html', context)

def add_book(request):
    if request.method == "POST":
        Book.objects.create(title= request.POST['title'], desc= request.POST['desc'])
    return redirect('/')

def books(request, book_id):
    context={
        'book': Book.objects.get(id= book_id),
        'other_authors': Author.objects.exclude(books__id= book_id)
    }
    return render(request, 'book.html', context)
    
def extra_author(request, book_id):
    this_book= Book.objects.get(id = book_id)
    author= Author.objects.get(id= request.POST['other_author'])
    this_book.authors.add(author)
    return redirect(f'/books/{book_id}')

def authors(request):
    context= {
        'all_authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def add_author(request):
    Author.objects.create(first_name= request.POST['first_name'], last_name= request.POST['last_name'], notes= request.POST['notes'])
    return redirect('/authors')

def authors_info(request, author_id):
    this_author= Author.objects.get(id= author_id)
    context= {
        'author': this_author,
        'all_books': Book.objects.exclude(authors__id= author_id)
    }
    return render(request, 'author_info.html', context)

def extra_book(request, author_id):
    this_author= Author.objects.get(id= author_id)
    book= Book.objects.get(id = request.POST['other_book'])
    this_author.books.add(book)
    return redirect(f"/authors/{author_id}")

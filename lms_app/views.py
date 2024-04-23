from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.
def saveCat(request):
    if request.method == 'POST':   
        addcat = CategoryForm(request.POST)
        if addcat.is_valid():
            addcat.save()

def index(request):
    if request.method == 'POST':   
        addbook = BookForm(request.POST, request.FILES)
        if addbook.is_valid():
            addbook.save()

    saveCat(request)
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'form': BookForm(),
        'catForm': CategoryForm(),
        'allbooks':Book.objects.filter(active=True).count(),
        'booksold':Book.objects.filter(status='sold').count(),
        'bookrented':Book.objects.filter(status='rented').count(),
        'bookavailable':Book.objects.filter(status='available').count(),
    }
    return render(request, 'pages/index.html', context)

def books(request):

    saveCat(request)

    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'catForm': CategoryForm(),
    }
    return render(request, 'pages/books.html', context)

def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid:
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)

    context = {
        'form':book_save
    }
    return render(request, 'pages/update.html', context)

def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
        
    return render(request, 'pages/delete.html')
from django.shortcuts import render, redirect
from firebase_admin import db
from LibrarySystem import firebase_config  # ensure it's loaded
import uuid

def home(request):
    ref = db.reference('library')
    books = ref.get()
    return render(request, 'home.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        book_id = str(uuid.uuid4().int)[:5]  # short numeric ID
        data = {
            'book_title': request.POST['book_title'],
            'author_name': request.POST['author_name'],
            'genre': request.POST['genre'],
        }
        db.reference(f'library/{book_id}').set(data)
        return redirect('home')
    return render(request, 'library/add_book.html')

def update_book(request, book_id):
    if request.method == 'POST':
        data = {
            'book_title': request.POST['book_title'],
            'author_name': request.POST['author_name'],
            'genre': request.POST['genre'],
        }
        db.reference(f'library/{book_id}').update(data)
        return redirect('home')
    book = db.reference(f'library/{book_id}').get()
    return render(request, 'library/update_book.html', {'book_id': book_id, 'book': book})

def delete_book(request, book_id):
    db.reference(f'library/{book_id}').delete()
    return redirect('home')


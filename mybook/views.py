from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


def first_page(request):
    book_list = Book.objects.all()

    return render(request, './index.html', {

        'book_list': book_list,

    })


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, './book_detail.html', {'book': book})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, './book_form.html', {

        'form': form}
                  )


def book_del(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('home')
    return render(request, 'book_del.html', {'book': book})


def book_update(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form, 'book': book})

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from book_store.models import Book


def first_view(request):

    # return HttpResponse('dddd')
    if request.method == 'GET':
        return render(request,'book_store/first_view.html')

def add_book(request):
    if request.method == 'GET':
        return render(request,'book_store/add_book.html')

    elif request.method == 'POST':

        try:
            bookname = request.POST.get('bookname')
            price = float(request.POST.get('price'))
            marketprice = float(request.POST.get('marketprice'))
            pub = request.POST.get('pub')
        except Exception:
            dict1 = {'res': 'xx'}
            return render(request,'book_store/add_book.html',dict1)

        obj = Book(bookname=bookname,price=price,marketprice=marketprice,pub=pub)
        obj.save()

        dict1 = {'res':1}
        return render(request, 'book_store/add_book.html', dict1)

def book_list(request):
    if request.method == 'GET':

        books = Book.objects.all()

        return render(request,'book_store/book_list.html',locals())

def update_book(request,book_id):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=book_id)
        except Exception:
            dict1 = {'res': 'no'}
            return render(request, 'book_store/update_book.html', dict1)

        return render(request,'book_store/update_book.html',locals())

    elif request.method == 'POST':
        try:
            new_price = float(request.POST.get('newmprice'))
        except Exception:
            dict1 = {'res':'xx'}
            return render(request,'book_store/update_book.html',dict1)

        book = Book.objects.get(id=book_id)

        book.marketprice = new_price

        book.save()

        dict1 = {'res':'yes'}

        # return HttpResponseRedirect('book_store/first_view.html')

        return render(request, 'book_store/update_book.html', dict1)


def delete_book(request,book_id):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=book_id)
        except Exception:
            dict1 = {'res': 'notfind'}
            return render(request, 'book_store/book_list.html', dict1)

        book.delete()

        return HttpResponseRedirect('/bookstore/book_list')






from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.shortcuts import get_object_or_404

def index(request):
	books=Book.objects.all()
	context={
		"books":books
	}
	return render(request,"book_outlet/index.html",context)

def book_details(request,id):
	#try:
	#	book=Book.objects.get(id=id)
	#except:
	#	raise Http404()
	book=get_object_or_404(Book,id=id)
	context={
	"title":book.title,
	"rating":book.rating,
	"is_bestseller":book.is_bestselling,
	"author":book.author
	}
	return render(request,"book_outlet/book_details.html",context)
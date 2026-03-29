from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Avg

def index(request):
	books=Book.objects.all().order_by("-title")
	for book in books:
		print(book.get_absolute_url())
		#print(book.title)
	context={
		"books":books,
		"total_books":books.count(),
		"average_rating":books.aggregate(Avg("rating"))["rating__avg"]
	}
	return render(request,"book_outlet/index.html",context)

def book_details(request,slug):
	#try:
	#	book=Book.objects.get(id=id)
	#except:
	#	raise Http404()
	book=get_object_or_404(Book,slug=slug)
	context={
	"id":book.id,
	"title":book.title,
	"rating":book.rating,
	"is_bestseller":book.is_bestselling,
	"author":book.author
	}
	return render(request,"book_outlet/book_details.html",context)
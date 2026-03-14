from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def january(request, *args, **kwargs):
	return HttpResponse("This is January challange.")

def february(request, *args, **kwargs):
	return HttpResponse("This is February challange.")
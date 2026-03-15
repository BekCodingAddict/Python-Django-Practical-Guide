from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseNotFound

# Create your views here.
def january(request, *args, **kwargs):
	return HttpResponse("This is January challange.")

def february(request, *args, **kwargs):
	return HttpResponse("This is February challange.")

def monthly_challange(request, month, *args, **kwargs):
	challanges = {
		"january": "This is January challange.",
		"february": "This is February challange.",
		"march": "This is March challange.",
		"april": "This is April challange.",
		"may": "This is May challange.",
		"june": "This is June challange.",
		"july": "This is July challange.",
		"august": "This is August challange.",
		"september": "This is September challange.",
		"october": "This is October challange.",
		"november": "This is November challange.",
		"december": "This is December challange."
	}

	challange_text = challanges.get(month, None)

	if challange_text == None:
		return HttpResponseNotFound("This month is not supported.")
	else:
		return HttpResponse(challange_text)
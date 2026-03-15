from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

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

# Create your views here.
def january(request, *args, **kwargs):
	return HttpResponse("This is January challange.")

def february(request, *args, **kwargs):
	return HttpResponse("This is February challange.")

def monthly_challange(request, month, *args, **kwargs):
	challange_text = challanges.get(month, None)
	if challange_text == None:
		return HttpResponseNotFound("This month is not supported.")
	else:
		return HttpResponse(challange_text)
	
def monthly_challange_by_number(request, month, *args, **kwargs):
	months = list(challanges.keys())
	if month > len(months):
		return HttpResponseNotFound("This month is not supported.")
	else:
		redirect_month = months[month-1]
		redirect_path = reverse("monthly-challange", args=[redirect_month])
		return HttpResponseRedirect(redirect_path)
	
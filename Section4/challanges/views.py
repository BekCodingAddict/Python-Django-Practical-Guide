from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
def index	(request, *args, **kwargs):
	html_="""
	<ul>
		<li><a href="/challanges/january">January</a></li>
		<li><a href="/challanges/february">February</a></li>
		<li><a href="/challanges/march">March</a></li>
		<li><a href="/challanges/april">April</a></li>
		<li><a href="/challanges/may">May</a></li>
		<li><a href="/challanges/june">June</a></li>
		<li><a href="/challanges/july">July</a></li>
		<li><a href="/challanges/august">August</a></li>
		<li><a href="/challanges/september">September</a></li>
		<li><a href="/challanges/october">October</a></li>
		<li><a href="/challanges/november">November</a></li>
		<li><a href="/challanges/december">December</a></li>
	</ul>
	"""
	return HttpResponse(html_)


def monthly_challange(request, month, *args, **kwargs):
	challange_text = challanges.get(month, None)
	context = {
		"month": month,
		"challange": challange_text
		}
	if challange_text == None:
		return HttpResponseNotFound("This month is not supported.")
	else:
		return render(request, "chellanges/challange.html", context)

def monthly_challange_by_number(request, month, *args, **kwargs):
	months = list(challanges.keys())
	if month > len(months):
		return HttpResponseNotFound("This month is not supported.")
	else:
		redirect_month = months[month-1]
		redirect_path = reverse("monthly-challange", args=[redirect_month])
		return HttpResponseRedirect(redirect_path)
	
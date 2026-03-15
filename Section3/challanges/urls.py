

from django.urls import path
from . import views

urlpatterns = [
	path('<int:month>', views.monthly_challange_by_number, name='monthly-challange-by-number'),
	path('<str:month>', views.monthly_challange, name='monthly-challange'),
]
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path("posts/", views.posts, name='posts'),
	path("posts/(?P<slug>[\w-]+)/", views.post_detail, name='post_detail'),
]
from django.shortcuts import render
from django.http import Http404

all_posts = [
	{
		"slug": "exploring-the-mountains",
		"title": "Exploring the Mountains",
		"image": "mountains.jpg",
		"author": "Asif",
		"date": "March 10, 2026",
		"excerpt": "Discover the beauty and adventure that awaits in the world's most breathtaking mountain ranges.",
		"content": "Mountains have always been a source of inspiration and adventure for those who seek the extraordinary. From the snow-capped peaks of the Himalayas to the rugged trails of the Rockies, every mountain range has a unique story to tell. Hiking through these natural wonders offers not just physical challenges but also moments of profound peace and clarity. The crisp mountain air, the panoramic views from the summit, and the sense of accomplishment after a long climb make every trip worthwhile. Whether you're a seasoned mountaineer or a beginner looking for your first trail, the mountains welcome all with open arms.",
	},
	{
		"slug": "django-for-beginners",
		"title": "Django for Beginners",
		"image": "coding.jpg",
		"author": "Asif",
		"date": "March 15, 2026",
		"excerpt": "A beginner-friendly guide to getting started with Django, the popular Python web framework.",
		"content": "Django is one of the most popular web frameworks for Python, and for good reason. It follows the 'batteries included' philosophy, providing everything you need to build robust web applications right out of the box. From its powerful ORM to the built-in admin panel, Django makes web development fast and enjoyable. In this guide, we walk through setting up your first Django project, creating views, templates, and URL patterns. By the end, you'll have a solid foundation to build upon and the confidence to tackle more complex projects.",
	},
	{
		"slug": "healthy-eating-habits",
		"title": "Healthy Eating Habits",
		"image": "food.jpg",
		"author": "Asif",
		"date": "March 20, 2026",
		"excerpt": "Simple and practical tips for developing healthy eating habits that last a lifetime.",
		"content": "Good nutrition is the foundation of a healthy life. But with so much conflicting information out there, it can be hard to know where to start. The key is to focus on whole, unprocessed foods — fruits, vegetables, lean proteins, and whole grains. Meal planning and preparation can help you stay on track, even on busy days. Remember, healthy eating isn't about strict diets or depriving yourself. It's about making consistent, mindful choices that nourish your body and mind. Start small, stay consistent, and the results will follow.",
	},
]


def home(request):
	latest_posts = all_posts[:3]
	return render(request, 'blog/index.html', {"posts": latest_posts})


def posts(request):
	return render(request, 'blog/all_posts.html', {"posts": all_posts})


def post_detail(request, slug):
	post = next((p for p in all_posts if p["slug"] == slug), None)
	if post is None:
		raise Http404("Post not found")
	return render(request, 'blog/post_detail.html', {"post": post})

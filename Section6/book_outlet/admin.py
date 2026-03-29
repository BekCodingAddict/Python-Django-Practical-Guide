from django.contrib import admin
from .models import Book,Author

class BookAdmin(admin.ModelAdmin):
	list_display = ("title","author","rating","is_bestselling")
	prepopulated_fields = {"slug":("title",)}
	list_filter = ("author","rating")
	search_fields = ("title","author")

class AuthorAdmin(admin.ModelAdmin):
	list_display = ("first_name","last_name")
	search_fields = ("first_name","last_name")
	list_filter = ("first_name","last_name")
	

# Register your models here.
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)

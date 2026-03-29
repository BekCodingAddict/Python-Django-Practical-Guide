from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Address(models.Model):
	street=models.CharField(max_length=100)
	postal_code=models.CharField(max_length=20)
	city=models.CharField(max_length=50)


	def __str__(self):
		return f"{self.street}, {self.postal_code}, {self.city}"


class Author(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	bio=models.TextField()
	address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True,related_name="author_address")

	def full_name(self):
		return f"{self.first_name} {self.last_name}"


	def __str__(self):
		return self.full_name()
	


class Book(models.Model):
	title = models.CharField(max_length=100)
	rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	author=models.ForeignKey(Author, on_delete=models.CASCADE,null=True,related_name="books")
	is_bestselling=models.BooleanField(default=False)
	slug=models.SlugField(default="",blank=True,null=False,db_index=True)


	def get_absolute_url(self):
		return reverse("book-details",args=[self.slug])
	
	#def save(self,*args,**kwargs):
	#	self.slug=slugify(self.title)
	#	super().save(*args,**kwargs)

	def __str__(self):
		return f"{self.title} by {self.author} (Rating: {self.rating}/5, Bestseller: {self.is_bestselling})"
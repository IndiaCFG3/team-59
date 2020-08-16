from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    INCOME_GROUP =(
		('belowAverage', 'belowAverage'),
		('average','average'),
		('aboveAverage', 'aboveAverage'))
    GENDER_TYPE = (
        ('Male','Male'),
        ('Female', 'Female'),
        ('LGBTQ','LGBTQ')
    )
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    income = models.FloatField(null=True)
    income_category = models.CharField(max_length=200, null=True, choices=INCOME_GROUP)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER_TYPE)
    def __str__(self):
    	return self.name

class volunteer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Scheme(models.Model):
	GENDER_TYPE = (
        ('Male','Male'),
        ('Female', 'Female'),
        ('LGBTQ','LGBTQ')
    )
	name = models.CharField(max_length=200, null=True)
	income_category= models.CharField(max_length=200, null=True)
	gender = models.CharField(max_length=200, choices=GENDER_TYPE, null=True)
	state = models.CharField(max_length=200, null=True)
	customer= models.ForeignKey(Customer, on_delete=models.CASCADE) 
	#any other parameters
	def __str__(self):
		return self.name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    INCOME_GROUP = (
		('belowAverage', 'belowAverage'),
		('average','average'),
		('aboveAverage', 'aboveAverage')
	)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    GENDER_TYPE = (
        ('Male','Male'),
        ('Female', 'Female'),
        ('LGBTQ','LGBTQ')
    )
    gender = models.CharField(max_length=200, null=True, choices=GENDER_TYPE)
    income = models.FloatField(null=True)
    income_category = models.CharField(max_length=200, null=True, choices=INCOME_GROUP)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone = models.IntegerField()
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=300)

class user_model(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to="userimg/",blank=True)
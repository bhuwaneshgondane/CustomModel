from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.IntegerField(( "Phone Number"))
    gender = models.CharField(choices=[ ('Male',"Male" ), ("Female","Female"),("Other","Other")], max_length=7)
    country = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=64,null=True)
    city = models.CharField(max_length=64,null=True)
    address = models.TextField(null=True)
    landmark = models.TextField(null=True)
    pincode = models.IntegerField(null=True)
    
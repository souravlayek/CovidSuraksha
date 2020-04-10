from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator,MinValueValidator


class MyUser(AbstractUser):
    usertype = models.CharField(max_length=50, choices=(
        ('doctor', 'Doctor'),
        ('user', 'Normal User'),
        ('shopmanager', 'Shop Manager')
    ))
    profileupdated = models.BooleanField(default=False)

class DoctorProfile(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    hospital_name = models.CharField(max_length=50)
    specialist_in = models.CharField(max_length=50)
    profilepic = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    def __str__(self):
        return self.user.username

class ShopManagerProfile(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    occupation = models.CharField(max_length=50)
    profilepic = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    notes = models.CharField(max_length=250, null=True)
    def __str__(self):
        return self.user.username

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    massage = models.CharField(max_length=250)


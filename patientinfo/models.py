from django.db import models
from accounts.models import MyUser
from django.utils.timezone import datetime
from django.core.validators import MaxValueValidator,MinValueValidator



# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    dateofinfection = models.DateField()
    age = models.IntegerField(validators=[MaxValueValidator(150)])
    admited_hospital = models.CharField(max_length=50)
    notes = models.CharField(max_length=250)
    gender = models.CharField(max_length=50, choices=(('male',"Male"),('female','Female')))
    address = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    district = models.CharField(max_length=50) 
    state = models.CharField(max_length=50)
    pin = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    def __str__(self):
        return self.username
    

class PatientInfo(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        MyUser, on_delete=models.CASCADE)
    medicine = models.CharField(max_length=50)
    condition = models.CharField(max_length=250)
    notes = models.CharField(max_length=250)
    time = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.patient.name
    
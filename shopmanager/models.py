from django.db import models
from django.core.validators import MaxValueValidator
from accounts.models import ShopManagerProfile

class Shop(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(ShopManagerProfile, on_delete=models.CASCADE)
    shoptype = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    phno = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    pendingitems= models.IntegerField(null=True)
    def __str__(self):
        return self.name

class ItemQuerry(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    items = models.CharField(max_length=500)
    pending = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    appoinment = models.CharField(max_length=50,null=True)
    notes = models.CharField(null=True,max_length=500)


# class Appoinment(models.Model):
#     item = models.ForeignKey(ItemQuerry, on_delete=models.CASCADE)
#     appoinment = models.DateTimeField()
#     notes = models.CharField(null=True,max_length=500)


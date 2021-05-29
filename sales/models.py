from django.db import models
from products.models import Products
from profiles.models import Profiles
from customers.models import Customer
from django.utils import timezone
from .utils import generate_code
from django.shortcuts import reverse

# Create your models here.
class Position(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField()
    price=models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    def save(self, *args,**kwargs):
        self.price = self.product.price *  self.quantity
        return super().save(*args,**kwargs)

    def __str__(self):
        return f"id: {self.id},product: {self.product.name}, quantity: {self.quantity}"

class Sale(models.Model):
    transaction_id = models.CharField(max_length=100,blank=True)
    positions = models.ManyToManyField(Position)
    total = models.FloatField(blank=True,null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sales for the amount of ${self.total}"

    def save(self, *args,**kwargs):
        if self.transaction_id == "" :
            self.transaction_id = generate_code()
        if self.created is None:
            self.created= timezone.now()
        return super().save(*args,**kwargs)

    def get_postions(self):
        return self.positions.all()

    def get_absolute_url(self):
        return reverse("sales:detail", kwargs={"pk": self.pk})
    

class CSV(models.Model):
    filename =models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"str({self.filename})"
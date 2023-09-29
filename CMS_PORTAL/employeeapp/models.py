from django.db import models
from adminapp.models import Employee_Creation
from django.contrib.auth.models import User 

# Create your models here.
class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100, null=False)
    company_name = models.CharField(max_length=100, null=False)
    product_image = models.ImageField(upload_to='media/')
    product_price = models.IntegerField()
    employee = models.ManyToManyField(Employee_Creation)   
    #employee = models.ForeignKey(Employee_Creation, on_delete=models.CASCADE)   #change 1
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    class Meta:
        db_table = "product"
        verbose_name_plural = "Employee_Product Panel"

class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    doc_specialisation = (("Chest","Chest"),("Heart","Heart"),("General","General"),("Orthopaedics","Orthopaedics"))
    contact = models.IntegerField()
    location = models.CharField(max_length=100, null=False)
    specialisation = models.CharField(max_length=100, choices=doc_specialisation, default="NA")    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "doctor"
        verbose_name_plural = "Doctor Panel"

class Appointment(models.Model):
    id = models.IntegerField(primary_key=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee_Creation, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        db_table = "appointment"
        verbose_name_plural = "Appointment Panel"

class Deals(models.Model):
    id = models.IntegerField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee_Creation, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    date = models.DateTimeField()
    quantity = models.IntegerField()

    class Meta:
        db_table = "deals"
        verbose_name_plural = "Deals Products Panel"
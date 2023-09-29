from django.db import models
from django.contrib.auth.models import User 

class Employee_Creation(models.Model):
    id = models.IntegerField(primary_key=True)
    #id = models.IntegerField(max_length=100,primary_key=True)
    first_name = models.CharField(max_length=100,default="NA")
    last_name = models.CharField(max_length=100,default="NA")
    email = models.EmailField(max_length=100,unique=True, default="NA")
    password = models.CharField(max_length=100,default="NA")
    doj = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = "employee_table"
        verbose_name_plural = "Employee Panel"

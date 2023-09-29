from django.contrib import admin
from adminapp.models import Employee_Creation
from employeeapp.models import Products, Doctor, Appointment, Deals
from django.utils.html import format_html
# Register your models here.

class CustomAdminProduct(admin.ModelAdmin):
    list_display = ['product_name','company_name','product_price','img_display','user_id']
    list_filter = ['product_name', 'company_name']
    list_per_page = 5
    search_fields = ['product_name', 'company_name', 'product_price']
    def img_display(self,obj):
        return format_html('<img src={} width="90" height="90" />',obj.product_image.url)    

class CustomAdminEmployee(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','password','doj','status']
    list_filter = ['first_name', 'last_name','email','status']
    list_per_page = 5
    search_fields = ['first_name', 'email', 'status']

class CustomAdminDoctor(admin.ModelAdmin):
    list_display = ['id','name','specialisation','location','contact']
    list_filter = ['name', 'specialisation']
    list_per_page = 5
    search_fields = ['name', 'specialisation', 'location']

class CustomAdminAppointment(admin.ModelAdmin):
    list_display = ['id','doctor','employee','date']
    list_filter = ['doctor', 'employee']
    list_per_page = 5
    search_fields = ['doctor', 'employee']    

class CustomAdminDeals(admin.ModelAdmin):
    #list_display = ['id','doctor','employee','product','date']
    #list_filter = ['doctor', 'employee','product']
    list_per_page = 5
    #search_fields = ['doctor', 'employee','product']    
    
admin.site.register(Products,CustomAdminProduct)
admin.site.register(Employee_Creation,CustomAdminEmployee)
admin.site.register(Doctor,CustomAdminDoctor)
admin.site.register(Appointment, CustomAdminAppointment)
admin.site.register(Deals,CustomAdminDeals)

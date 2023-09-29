from django.contrib import admin
from django.urls import path
from employeeapp.views import Employee_Module
from django.contrib import messages
from . import views


# Below somewhere there may be aproblem with page ALL Employee or All Product database drop down list
#please go to their respective html page and search the desciption error at line no above 45
urlpatterns = [    
    path('employee_home', Employee_Module.home, name="employee_home"),     
    path('logout/',Employee_Module.logout_view, name="employeelogout"),
    path('product_details', Employee_Module.product_details, name="product_details"),
    path('add_products', Employee_Module.add_products, name="add_products"),
    path('add_product_details', Employee_Module.add_product_details, name="add_product_details"),
    path('add_doctors', Employee_Module.add_doctors, name="add_doctors"),
    path('deals_details', Employee_Module.deals_details, name="deals_details"),
    path('add_deals', Employee_Module.add_deals, name="add_deals"),
    path('appointment', Employee_Module.add_appointment, name="appointment"),
    path('schedule', Employee_Module.schedule, name="schedule"),
]
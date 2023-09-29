from django.contrib import admin
from django.urls import path
from adminapp.views import Admin_Module
from django.contrib import messages
from . import views

urlpatterns = [
    path('admin_home', Admin_Module.home, name="admin_home"),
    path('register', Admin_Module.register, name='register'),    
    path('error404', Admin_Module.error404, name='error404'), 
    path('blank', Admin_Module.blank, name='blank'),
    path('buttons',Admin_Module.buttons, name='buttons'),
    path('cards', Admin_Module.cards, name='cards'),
    path('charts', Admin_Module.charts, name='charts'),
    path('forgot_password', Admin_Module.forgot_password, name='forgot_password'),
    path('tables', Admin_Module.tables, name='tables'),
    path('utilities_animation', Admin_Module.utilities_animation, name='utilities_animation'),
    path('utilities_border', Admin_Module.utilities_border, name='utilities_border'),
    path('utilities_color', Admin_Module.utilities_color, name='utilities_color'),
    path('utilities_other', Admin_Module.utilities_other, name='utilities_other'),
    path('dashboard', Admin_Module.dashboard, name="admin_dashboard"),
    path('search_employee',Admin_Module.search, name='search_employee'),
    path('dropdown/<str:pk>',Admin_Module.dropdown, name='dropdown'),
    path('create_employee',Admin_Module.create, name='create_employee'),
    path('edit',Admin_Module.editemployee, name='edit'),
    path('edit_employee',Admin_Module.edit, name='edit_employee'),
    path('admin_dashboard', Admin_Module.DatabaseAdmin,name="admin_dashboard"),
    path('visit_details',Admin_Module.visit_details, name='visit_details'),
    path('my_profile',Admin_Module.my_profile, name='my_profile'),
    path('settings',Admin_Module.settings, name='settings'),
]

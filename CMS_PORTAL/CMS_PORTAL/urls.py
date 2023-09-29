"""
URL configuration for Hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from adminapp.views import Admin_Module, AdminLogin, AdminLogout
from employeeapp.views import EmployeeLogin
from django.contrib import messages
#from . import views

urlpatterns = [
    path('', Admin_Module.CMS, name='home-page'),
    path('admin/', admin.site.urls),
    path('adminapp/', include('adminapp.urls')),    
    path('employeeapp/', include('employeeapp.urls')),        
    path('admin_home/login/',AdminLogin.as_view(template_name='login.html'),name='admin_login'),
    path('logout/',AdminLogout.as_view(),name='adminlogout'),    
    #path('logout/',EmployeeLogout.as_view(),name='employeelogout'),
    path('employee_home/login/',EmployeeLogin.as_view(template_name='login.html'), name='employee_login'),
    #path('login',AdminLogin.as_view(template_name='login.html'), name='login'),
    #path('logout/',AdminLogout.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
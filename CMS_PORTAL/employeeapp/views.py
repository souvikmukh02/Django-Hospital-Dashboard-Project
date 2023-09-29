from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from adminapp.models import Employee_Creation
from employeeapp.models import Products, Doctor, Appointment, Deals
from django.contrib.auth.views import LoginView
from adminapp.forms import RegistrationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import logout
import datetime

# Create your views here.
class Employee_Module(View):    
    def home(request):

        user = request.user
        objects = {
            'obj0':'active',
            'obj1': '',
            'obj2': 'collapsed',
            'obj3': '',
            'obj4': '',
            'obj5': 'collapsed',
            'obj6': '',
            'obj7': '',
            'obj8': 'collapsed',
            'obj9': '',
            'obj10': '',
            'obj11': '',
            'obj12': '',
            'obj13': '',
            'obj14': '',
            'obj15': '',
            'obj16': '',
            'obj17': '',
            'obj18': '',
            'obj19': '',
            'obj20': '',
            'obj21': '',
            'obj22': '',
            'user': user,
        }        
        return render(request, 'home.html', objects)        
            

    def product_details(request):        
        user = request.user        
        user_id = request.user.id
        emp_email = request.user.email
        emp = Employee_Creation.objects.get(user_id=user_id)
                
        notmyproduct = []        
        if request.POST.get('product'):
            product_id = request.POST.get('product')
            Products.objects.filter(id=product_id).update(employee_id=emp.id)

        else:
            
            query = "Select * from product_employee where not employee_creation_id ='"+str(emp.id)+"' "
            notmyproduct = Products.objects.raw(query)
        
        data = Products.objects.filter(user_id=user_id)          
        info = Products.objects.all()
        employee_name = Employee_Creation.objects.get(user_id=user_id).first_name +" "+ Employee_Creation.objects.get(user_id=user_id).last_name

        objects = {
            'obj0': '',
            'obj1': 'active',
            'obj2': '',
            'obj3': 'show',
            'obj4': '',
            'obj5': 'collapsed',
            'obj6': '',
            'obj7': '',
            'obj8': 'collapsed',
            'obj9': '',
            'obj10': '',
            'obj11': '',
            'obj12': 'active',
            'obj13': '',
            'obj14': '',
            'obj15': '',
            'obj16': '',
            'obj17': '',
            'obj18': '',
            'obj19': '',
            'obj20': '',
            'obj21': '',
            'obj22': '',
            'products': data,
            'allproducts': info,
            'otherproducts': notmyproduct,            
            'employee_name': employee_name,
            'user': user,
        }        
        return render(request, 'products.html', objects)

    def add_product_details(request):
        email = User.objects.get(username=request.user).email
        user = request.user
        employee_id = Employee_Creation.objects.get(user_id=user.id).first_name +" "+ Employee_Creation.objects.get(user_id=user.id).last_name
        context = {
            'user_id': 1,
            'employee_id': employee_id,
            'user': user,
        }
        return render(request,'product_add.html', context)

    def add_products(request):
        user = request.user
        # add to employee-product table not working through insert
        product_name = request.POST.get('product_name')
        company_name = request.POST.get('company_name')
        product_image = request.POST.get('product_image')
        product_price = request.POST.get('product_price')
        email = User.objects.get(username=request.user).email
        employee_id = Employee_Creation.objects.filter(email=email)        
        user_id = request.user.id        
        employee_id = Employee_Creation.objects.get(email=email).id
        employee_name = Employee_Creation.objects.get(email=email).first_name +" "+ Employee_Creation.objects.get(email=email).last_name
        #check if it takes autoid
        Products.objects.create(product_name=product_name,company_name=company_name,product_image=product_image,product_price=product_price, user_id=user_id)
        data = Products.objects.filter(user_id=user_id)
        for item in data:
            if item.product_name == product_name:
                product_id = item.id                
        info = Products.objects.all()

        context = {
            'products': data,
            'allproducts': info,
            'employee_name':employee_name,
            'user': user,
        }
        messages.success(request, 'Product Details Created Successfully by '+employee_name)
        return render(request,'products.html', context)

    def add_doctors(request):
        user = request.user
        if request.POST.get('doctor_name'):
            name = request.POST.get('doctor_name')
            specialisation = request.POST.get('specialization')
            location = request.POST.get('location')
            contact = request.POST.get('contact')            
            value = Doctor.objects.filter(name=name) & Doctor.objects.filter(specialisation=specialisation)
            print(value)
            if value:
                print("Same doctor")
                messages.error(request, 'Doctor Details already present added by someone.')
            else:
                doctors = Doctor.objects.all()
                employee_name = user.first_name +" "+ user.last_name
                for doctor in doctors:
                    doctor_id = doctor.id+1
                Doctor.objects.create(name=name,specialisation=specialisation,location=location,contact=contact,user_id=request.user.id)
                messages.success(request, 'Doctor Details Added Successfully by '+employee_name)       
            
        doctors = Doctor.objects.filter(user_id=user.id)
        employee_name = user.first_name +" "+ user.last_name
        context = {
            'doctors': doctors,
            'employee_name': employee_name,
            'user':user,
        }        
        return render(request,'doctor_add.html',context)

    def add_appointment(request):
        user = request.user
        token = []
        date_today  = str(datetime.datetime.today())
        list1 = date_today.split(" ")        
        date_today = list1[0]
        if request.POST.get('doctor'):
            doctor_id = request.POST.get('doctor')
            date_of_appointment = request.POST.get('date')
            time_of_appointment = request.POST.get('time')
            empid = request.POST.get('employee')
            emp_name = Employee_Creation.objects.get(id=empid).first_name+" "+Employee_Creation.objects.get(id=empid).last_name
            Appointment.objects.create(date=date_of_appointment,time=time_of_appointment,doctor_id=doctor_id,employee_id=empid)
        else:
            emp = Employee_Creation.objects.get(user_id=user.id)
            empid = emp.id
            email = emp.email
            emp_name = emp.first_name+" "+emp.last_name

        appointment = Appointment.objects.filter(employee_id=empid) 
        for dates in appointment:
            doctor = Doctor.objects.get(id=dates.doctor_id).name            
            date = dates.date
            time = dates.time
            token.append([doctor,date,time,emp_name])
        doctor = Doctor.objects.all()
        
        context = {
            'date': date_today,
            'employeeid': empid,
            'employee': emp_name,
            'doctor':doctor,
            'appointment': token,
            'user':user,
        }
        return render(request,'utilities-other.html', context)

    def schedule(request):
        user = request.user
        token = []
        date = request.POST.get('date')
        user_id = request.user.id
        employee = Employee_Creation.objects.get(email=request.user.email)
        employee_id = employee.id
        emp_name = employee.first_name +" "+ employee.last_name
        appointment = Appointment.objects.filter(employee_id=employee_id) & Appointment.objects.filter(date=date)
        for schedule in appointment:
            doctor = Doctor.objects.get(id=schedule.doctor_id).name
            date = schedule.date
            time = schedule.time
            emp_name = emp_name
            token.append([doctor,date,time,emp_name])

        context = {
            'appointment': token,
            'user': user,
        }
        return render(request,'utilities-animation.html',context)

    def deals_details(request):
        user = request.user        
        doctor = Doctor.objects.all()
        product = Products.objects.all()
        email = User.objects.get(username=request.user).email
        employee = Employee_Creation.objects.get(email=email)        
        employeeid = employee.id
        deals = Deals.objects.filter(employee_id=employeeid)
        employee_name = employee.first_name +" "+employee.last_name
        context = {
            'deals': deals,  
            'doctor': doctor,          
            'product':product,
            'employee': employee,
            'employeeid': employeeid,
            'employee_name': employee_name,
            'user': user,            
        }        
        return render(request,'deals_add.html',context)
    
    def add_deals(request):
        user = request.user        
        employeeid = request.POST.get('employee')
        doctor_id = request.POST.get('doctor')
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')
        
        date = datetime.date.today()
        product = Products.objects.all()
        doctor = Doctor.objects.all()
        dealings = Deals.objects.all()
        for deal in dealings:
            deal_id = deal.id+1
        Deals.objects.create(doctor_id=doctor_id,product_id=product_id,quantity=quantity,employee_id=employeeid,date=date)
        deals = Deals.objects.filter(employee_id=employeeid)        
        product_name = Products.objects.filter(id=product_id)
        employee = Employee_Creation.objects.get(user_id=request.user.id)
        employee_name = employee.first_name+" "+employee.last_name
        context = {
            'deals':deals,
            'doctor': doctor,          
            'product':product,
            'doctor_name': doctor,
            'product_name':product_name,
            'employeeid': employee.id,
            'employee': employee,
            'employee_name':employee_name,
            'user': user,        
        }
        messages.success(request, 'Deals Details Added Successfully for '+employee_name)
        return render(request,'deals_add.html',context)

    def logout_view(request):
        user = User.objects.get(username=request.user)        
        if user.is_superuser:
            logout(request)
            return redirect('/')
        else: 
            employee = Employee_Creation.objects.filter(email=request.user.email)
            User.objects.filter(username=request.user).update(is_staff=0)
            employee.update(status=False)
            logout(request)
            return redirect('/')


class EmployeeLogin(LoginView):       
    def form_valid(self,form):               
        #changes done for multiple login
        username = form.cleaned_data.get('username')
        user = User.objects.filter(username=username)
        employee = Employee_Creation.objects.filter(email=user[0].email)
        user.update(is_staff=1)
        employee.update(status=True)
        messages.success(self.request,"Logged In Successfully.")
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"Invalid Credentials.")
        return super().form_invalid(form)

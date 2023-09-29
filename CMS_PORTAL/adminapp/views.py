from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from adminapp.models import Employee_Creation
from employeeapp.models import Products, Deals,Doctor, Appointment
from django.views import View
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
import datetime

# Create your views here.
class Admin_Module(View):

    def CMS(request):
        return render(request,'CMS_PORTAL.html')

    def DatabaseAdmin(request):
        return redirect('/admin/')
    
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
            'admin': user,
        }
        return render(request, 'index.html', objects)

    def buttons(request):
        user = request.user
        data = Employee_Creation.objects.all().order_by('id')

        form = RegistrationForm()         
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
            'employees': data,
            'form': form,
            'admin':user,
        }        
        return render(request, 'buttons.html', objects)
    
    def cards(request):
        user = request.user        
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
            'obj12': '',
            'obj13': 'active',
            'obj14': '',
            'obj15': '',
            'obj16': '',
            'obj17': '',
            'obj18': '',
            'obj19': '',
            'obj20': '',
            'obj21': '',
            'obj22': '',
            'admin':user,
        }
        return render(request, 'cards.html', objects)

    def utilities_color(request):
        user = request.user                
        data = Employee_Creation.objects.all()
        products = Products.objects.all()
        query = ""
        #products = Products.objects.raw(query)
        #products = Products.objects.all()
        #query2 = "Select employee_table.id, employee_table.first_name, employee_table.last_name, product.product_name, product.company_name, product.product_image from product inner join employee_table on product.employee_id=employee_table.id"
        #products = Products.objects.raw(query2)
        #emp_name =  []               
        objects = {
            'obj0': '',
            'obj1': '',
            'obj2': 'collapsed',
            'obj3': '',
            'obj4': 'active',
            'obj5': '',
            'obj6': 'show',
            'obj7': '',
            'obj8': 'collapsed',
            'obj9': '',
            'obj10': '',
            'obj11': '',
            'obj12': '',
            'obj13': '',
            'obj14': 'active',
            'obj15': '',
            'obj16': '',
            'obj17': '',
            'obj18': '',
            'obj19': '',
            'obj20': '',
            'obj21': '',
            'obj22': '',
            'employees_product': data,
            'products': products,
            #'employee_name':emp_name,            
            'admin':user,
        }        
        return render(request, 'utilities-color.html', objects)

    def utilities_border(request):                         
        user = request.user
        emp = {'Begin'}
        emp_name = set()
        data = []
        quantity = []
        product_name = []        
        doctor_name = []
        deals_month = []
        data = Employee_Creation.objects.all()

        if request.POST.get('employees'):
            empid = request.POST.get('employees')       #this is a string not integer
            monthofyear = request.POST.get('date')
            deals_date = Deals.objects.filter(date__month=monthofyear)            

            if empid=="0":
                deals = deals_date
            else:
                deals = Deals.objects.filter(employee_id=empid) & deals_date
            
            for item in deals:
                emp.add(Employee_Creation.objects.get(id=item.employee_id).first_name+" "+Employee_Creation.objects.get(id=item.employee_id).last_name)
                if emp_name in emp:
                    continue
                else:
                    emp_name = {Employee_Creation.objects.get(id=item.employee_id).first_name+" "+Employee_Creation.objects.get(id=item.employee_id).last_name}
                    user_id = Employee_Creation.objects.get(id=item.employee_id).user_id
                    products = Products.objects.filter(id=item.product_id) & Products.objects.filter(user_id=user_id)
                    doctors = Doctor.objects.filter(id=item.doctor_id) & Doctor.objects.filter(user_id=user_id)
                    for x in products:
                        quantity.append(Deals.objects.get(product_id=x.id).quantity)
                        product_name.append(x.product_name)
                    for y in doctors:
                        doctor_name.append(y.name)
                    deals_month.append([doctor_name,product_name,quantity,emp_name])
                    product_name = []
                    doctor_name = []
                    quantity = []                
            
                

        objects = {
            'obj0': '',
            'obj1': '',
            'obj2': 'collapsed',
            'obj3': '',
            'obj4': 'active',
            'obj5': '',
            'obj6': 'show',
            'obj7': '',
            'obj8': 'collapsed',
            'obj9': '',
            'obj10': '',
            'obj11': '',
            'obj12': '',
            'obj13': '',
            'obj14': '',
            'obj15': 'active',
            'obj16': '',
            'obj17': '',
            'obj18': '',
            'obj19': '',
            'obj20': '',
            'obj21': '',
            'obj22': '',
            'employees_product': data,
            'deals_month': deals_month,
            #'emp_name':emp_name,
            'product_name': product_name,
            'doctor_name': doctor_name,
            'admin':user,
        }
        return render(request, 'utilities-border.html', objects)

    def utilities_animation(request):
        user = request.user
        objects = {
            'obj0': '',
            'obj1': '',
            'obj2': 'collapsed',
            'obj3': '',
            'obj4': 'active',
            'obj5': '',
            'obj6': 'show',
            'obj7': '',
            'obj8': 'collapsed',
            'obj9': '',
            'obj10': '',
            'obj11': '',
            'obj12': '',
            'obj13': '',
            'obj14': '',
            'obj15': '',
            'obj16': 'active',
            'obj17': '',
            'obj18': '',
            'obj19': '',
            'obj20': '',
            'obj21': '',
            'obj22': '',
            'admin':user,
        }
        return render(request, 'utilities-animation.html', objects)

    def utilities_other(request):
        user = request.user
        objects = {
            'obj0': '',
            'obj1': '',
            'obj2': 'collapsed',
            'obj3': '',
            'obj4': 'active',
            'obj5': '',
            'obj6': 'show',
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
            'obj17': 'active',
            'obj18': '',
            'obj19': '',
            'obj20': '',
            'obj21': '',
            'obj22': '',
            'admin':user,
        }
        return render(request, 'utilities-other.html', objects)

    def forgot_password(request):
        return render(request, 'forgot-password.html')

    def error404(request):
        user = request.user
        objects = {
            'obj0': '',
            'obj1': '',
            'obj2': 'collapsed',
            'obj3': '',
            'obj4': '',
            'obj5': 'collapsed',
            'obj6': '',
            'obj7': 'active',
            'obj8': '',
            'obj9': 'show',
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
            'obj21': 'active',
            'obj22': '',
            'admin':user,
        }
        return render(request, '404.html', objects)

    def blank(request):
        user = request.user
        objects = {
            'obj0': '',
            'obj1': '',
            'obj2': 'collapsed',
            'obj3': '',
            'obj4': '',
            'obj5': 'collapsed',
            'obj6': '',
            'obj7': 'active',
            'obj8': '',
            'obj9': 'show',
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
            'obj22': 'active',
            'admin':user,
        }
        return render(request, 'blank.html', objects)

    def charts(request):
        user = request.user
        objects = {
            'obj0': '',
            'obj1': '',
            'obj2': 'collapsed',
            'obj3': '',
            'obj4': '',
            'obj5': 'collapsed',
            'obj6': '',
            'obj7': '',
            'obj8': 'collapsed',
            'obj9': '',
            'obj10': 'active',
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
            'admin':user,
        }
        return render(request, 'charts.html', objects)

    def tables(request):
        user = request.user
        objects = {
            'obj0': '',
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
            'obj11': 'active',
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
            'admin':user,
        }
        return render(request, 'tables.html', objects)

    def dashboard(request):
        info = {

        }
        return render(request, 'index.html', info)

    def create(request):
        user = request.user
        if request.POST.get('submit2'):
            data_all = Employee_Creation.objects.all()
            context = {
                'employees': data_all,
                'admin':user,
            }
            return render(request, 'buttons.html', context)
        else:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            doj = request.POST.get('doj')
            
            Employee_Creation.objects.create(first_name=first_name,last_name=last_name,email=email,password=password,doj=doj,status=False)
            data = Employee_Creation.objects.filter(first_name=first_name) & Employee_Creation.objects.filter(email=email)
            context = {
                'employees': data,
                'admin':user,
            }        
            return render(request, 'buttons.html', context)

    def editemployee(request):
        return render(request,'employee_edit.html')
    
    def edit(request):
        user = request.user
        if request.POST.get('submit2'):
            data_all = Employee_Creation.objects.all()
            context = {
                'employees': data_all,
                'admin':user,
            }
            messages.success(request, 'Refreshed')
            return redirect('/adminapp/admin_home')
        else:
            id = request.POST.get('empid')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            email2 = Employee_Creation.objects.get(id=id).email
            Employee_Creation.objects.filter(id=id).update(first_name=first_name,last_name=last_name,email=email)
            User.objects.filter(email=email2).update(first_name=first_name,last_name=last_name,email=email)

            data = Employee_Creation.objects.get(id=id)
            data_all = Employee_Creation.objects.all()
            
            context = {
                'emp_edit': data,
                'employees': data_all,
                'admin':user,
            }        
            messages.success(request, 'Employee Details Editted Successfully for '+first_name)
            return render(request, 'buttons.html', context)

    def visit_details(request):
        user = request.user
        visit = []
        emp = {'Begin'}
        emp_name = set()
        data = []
        time = []
        date = []        
        doctor_name = []
        data = Employee_Creation.objects.all()
        value = 0

        if request.POST.get('employees'):
            empid = request.POST.get('employees')       #this is a string not integer
            monthofyear = request.POST.get('date')
            appointment_date = Appointment.objects.filter(date__month=monthofyear)            
            value = 1

            if empid=="0":
                appointment = appointment_date
            else:
                appointment = Appointment.objects.filter(employee_id=empid) & appointment_date
            
            for item in appointment:
                emp_name = Employee_Creation.objects.get(id=item.employee_id).first_name+" "+Employee_Creation.objects.get(id=item.employee_id).last_name
                doctor_name = Doctor.objects.get(id=item.doctor_id).name
                date = item.date
                time = item.time
                visit.append([doctor_name,date,time,emp_name])                
        objects = {
            'obj0': '',
            'obj1': '',
            'obj2': 'collapsed',
            'obj3': '',
            'obj4': 'active',
            'obj5': '',
            'obj6': 'show',
            'obj7': '',
            'obj8': 'collapsed',
            'obj9': '',
            'obj10': '',
            'obj11': '',
            'obj12': '',
            'obj13': '',
            'obj14': '',
            'obj15': 'active',
            'obj16': '',
            'obj17': '',
            'obj18': '',
            'obj19': '',
            'obj20': '',
            'obj21': '',
            'obj22': '',
            'visit': visit,           
            'value': value,
            'employees_product': data,            
            'admin':user,
        }        
        return render(request,'charts.html',objects)

    def search(request):
        user = request.user
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')

        data = Employee_Creation.objects.filter(first_name=first_name) & Employee_Creation.objects.filter(email=email)
        print(data, email)
        context = {
            'employees': data,
            'admin':user,
        }
        return render(request, 'cards.html', context)

    def dropdown(request,pk): 
        user = request.user   
        data = []
        info = []
        allemp = []
        s_emp_name = []
        products = None
        if pk == "products":     
            if request.POST.get('submit'):   
                empid = request.POST.get('selector')
                print(empid)
                if int(empid) == 0:                                   
                    url = "utilities-color.html"
                else: 
                    emp = Employee_Creation.objects.get(id=empid)
                    employee_name= emp.first_name + emp.last_name
                    s_emp_name = emp
                    products = Products.objects.filter(user_id=emp.user_id)
                    allemp = Employee_Creation.objects.all()
                    url = "utilities-color.html"
            else: 
                products = Products.objects.all()
            
            url = "utilities-color.html"
        elif pk == "edit":            
            empid = request.POST.get('selector')
            products = []                       
            data = Employee_Creation.objects.get(id=empid)
            url = "buttons.html"
        elif pk == "deals":
            url = "utilities-border.html"   #modification requiered
        else:
            data = Employee_Creation.objects.get(id=empid)
        
        context = {
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
            'products': products,
            'emp_edit': data,
            'emp_data': data,
            'employees': info,
            'employees_product': allemp,
            's_emp_name':s_emp_name,
            'admin':user,
        }
        return render(request,url,context)
    
    def settings(request):
        user = request.user
        employees = Employee_Creation.objects.all()
        emp = None
        if request.POST.get('selector'):
            empid = request.POST.get('selector')                        
            email = Employee_Creation.objects.get(id=empid).email
            user_id = User.objects.get(email=email).id
            emp = User.objects.get(id=user_id)

        if request.POST.get('id'):
            user_id = request.POST.get('id')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            is_superuser = request.POST.get('is_superuser')  
            is_active = request.POST.get('is_active')                        
            email = User.objects.get(id=user_id).email
            User.objects.filter(id=user_id).update(first_name=first_name,last_name=last_name,is_superuser=is_superuser,is_active=is_active)
            Employee_Creation.objects.filter(email=email).update(first_name=first_name,last_name=last_name)
            emp = User.objects.get(id=user_id)
            messages.success(request, 'Employee SuperUser and Active Status Editted Successfully for '+first_name)

        if request.POST.get('delete'):
            empid = request.POST.get('delete')                        
            email = Employee_Creation.objects.get(id=empid).email
            user_id = User.objects.get(email=email).id
            Employee_Creation.objects.filter(id=empid).delete()
            User.objects.filter(id=user_id).delete()
            messages.success(request, 'Employee Deleted Successfully')
        context = {
            'emp': emp,
            'employees': employees,
        }        
        return render(request,'settings.html',context)
    
    def my_profile(request):
        user = User.objects.get(id=request.user.id)

        if request.POST.get('id'):
            user_id = request.POST.get('id')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            User.objects.filter(id=request.user.id).update(first_name=first_name,last_name=last_name,email=email)
            user  = User.objects.get(id=request.user.id)
            messages.success(request, 'Details Editted Successfully for '+first_name)
        context = {
            'administration': user, 
        }

        return render(request,'profile.html', context)

    def register(request):
        if request.method == "GET":
            form = RegistrationForm()
            return render(request,'register.html',{'form': form})

        if request.method == "POST":            
            form = RegistrationForm(request.POST)                        
            if form.is_valid():                
                form.save()
                username = form.cleaned_data.get('username')   
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                email =form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                employee = form.cleaned_data.get('check')
                data = User.objects.filter(username=username).update(is_staff=0)  
                userdata = User.objects.filter(username=username)
                for useronly in userdata:
                    user_id = useronly.id
                if employee:   
                    employees = Employee_Creation.objects.all()                                                                         
                    Employee_Creation.objects.create(first_name=first_name,last_name=last_name,email=email,password=password,status=False, user_id=user_id)
                    messages.success(request, 'Account Created Successfully for '+username)
                    return redirect('/adminapp/admin_home')                
                else: 
                    userdata.update(is_superuser=1,is_staff=1)
                    messages.success(request, 'Account Created Successfully for '+username)
                    return redirect('/adminapp/admin_home')
            else:
                messages.error(request, 'Some Entry Error')
                return render(request, 'register.html', {'form':form})


class AdminLogin(LoginView):    
    def form_valid(self,form):
        messages.success(self.request,"Logged In Successfully.")
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"Invalid Credentials.")
        return super().form_invalid(form)

class AdminLogout(LogoutView):
    def get_next_page(self):
        messages.success(self.request,"Logged Off Successfully. ")
        return reverse_lazy('home-page')

from django.shortcuts import render,redirect
from .models import QuesModel, loginmodel,Signupmodel,attendmodel
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def App_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        role = request.POST.get('role')
        userrecommend = request.POST.get('user-recommend')
        prefer = request.POST.get('prefer')
        Comment = request.POST.get('comment')
        print(name, email, age, role, userrecommend, prefer, Comment)
        register_form = QuesModel(name=name, email=email, role=role,
                         userrecommend=userrecommend, prefer=prefer, Comment=Comment)
        register_form.save()
        return render(request,'success.html')
    else:
        return render(request, 'Employee.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # form = loginmodel(username=username, password=password)
        # form.save()

        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            user_email = User.objects.get(username=username)
            if user_email.is_superuser:
                return render (request,'adm.html')
            else:
                return redirect("/display/")
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
def link_view(request):
    return render(request, 'link.html')

def list_view(request):
    users = QuesModel.objects.values()
    user_details = list(users)
    print(user_details)
    return render(request,'view.html',{'name': user_details})
def sign_view(request):
    if request.method == "POST":
        email= request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # remember = request.POST.get('remember')
 
        print(email,username, password)
        register_form = User.objects.create_user( email=email,username=username,
                         password=password)
        register_form.save()
        return render(request,'success.html')
    else:
        return render(request, 'signup.html')
def log_view(request):
    if request.method == "POST":
        # Empcode = request.POST.get('Empcode')
        empname = request.POST.get('empname')
        drpleavetypele = request.POST.get('drpleavetype')
        drpapplyingtyp = request.POST.get('drpapplyingtyp')
        Noofdays = request.POST.get('Noofdays')
        todate = request.POST.get('todate')
        fromdate = request.POST.get('fromdate')
        mobileno =  request.POST.get('mobileno')
        status =  request.POST.get('mobileno')

        print(empname, drpleavetypele, drpapplyingtyp, Noofdays, todate, fromdate, mobileno)
        register_form = attendmodel(Empname=empname, drpleavetypele=drpleavetypele,
                         drpapplyingtyp=drpapplyingtyp, Noofdays=Noofdays, todate=todate, fromdate=fromdate, mobileno=mobileno)
        register_form.save()
        return render(request,'success.html')
    else:
        return render(request, 'view.html')
def profile_view(request):
    return render(request, 'myprofile.html')
def leaveapprove_view(request):
   users =attendmodel.objects.values()
   user_details = list(users)
   print(user_details)
   return render(request,'leaveapprove.html',{'name': user_details})


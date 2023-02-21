from django.shortcuts import render,HttpResponse
from .models import login_page

def Reg_View(request):
   if request.method == "POST":
      fname = request.POST.get('fname')
      lname = request.POST.get('lname')
      email = request.POST.get('email')
      gender = request.POST.get('gender')
      print(fname,lname,email,gender)
      form = login_page(first_name=fname,last_name=lname,email=email,gender=gender)
      form.save()
      return render(request, 'Refer.html',{"fname": fname, "lname": lname, "email": email,"gender": gender})
   else:
      return render(request, 'Register.html')

# def Func(request):
#     fname = request.GET.get("fname")
#     lname = request.GET.get("lname")
#     email = request.POST.get('email')
#     gender = request.POST.get('gender')
#     print(fname, lname)
#     return render(request,'refer.html' , {"fname": fname, "lname": lname, "email": email, "gender": gender })





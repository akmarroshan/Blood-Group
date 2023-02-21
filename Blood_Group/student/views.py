from django.shortcuts import render
from .forms import StudentForm,Calculation

# Create your views here.
def load_page(request):  
    if request.method == "GET":
        form = StudentForm()  
        return render(request,"form_new.html",{'form':form})
    elif request.method == "POST":
        form_data = StudentForm(request.POST)
      
        if form_data.is_valid():
            firstname = form_data.cleaned_data['firstname']
            lastname = form_data.cleaned_data['lastname']
            print(firstname, lastname)
            return render(request, 'dis.html', {"fname": firstname, "lname": lastname})
def add_page(request):
    if request.method == "GET":
        form = Calculation()  
        return render(request,"addittion.html",{'form':form})
    elif request.method == "POST":
        form_data = Calculation(request.POST)
      
        if form_data.is_valid():
            firstbox = form_data.cleaned_data['firstbox']
            Secondbox = form_data.cleaned_data['Secondbox']
            total = int(firstbox) + int(Secondbox)
            print(total)
            return render(request, 'Sum.html', {"firstnumber": firstbox, "Secondnumber": Secondbox,"total" : total})

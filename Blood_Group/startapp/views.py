from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse
def homePageView(request):
    return render(request,'index.html')
def form(request):
    return render(request,'form.html')
def display(request):
    fname = request.GET.get("fname")
    lname = request.GET.get("lname")
    print(fname, lname)
    return render(request,'display.html' , {"fname": fname, "lname": lname})

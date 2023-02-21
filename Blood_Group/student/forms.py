from django import forms  
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)  
class Calculation(forms.Form):
    firstbox = forms.CharField(label="Enter first number",max_length=50)  
    Secondbox  = forms.CharField(label="Enter Second number", max_length = 100)  

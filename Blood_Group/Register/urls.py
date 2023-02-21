from django.urls import path
from .views import Reg_View
urlpatterns = [
    path('', Reg_View, name="register-form"),
    # path('add-form/'),  Func, name="add-form"),
   
]
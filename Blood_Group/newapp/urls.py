# pages/urls.py
from django.urls import path
from .views import login_page,App_view,link_view,list_view,sign_view,log_view,profile_view,leaveapprove_view


urlpatterns = [
    path("", login_page, name="home"),
    path("register/",App_view,name="form"),
    path("display/",link_view,name="display"),
    path("view/",list_view,name="view"),
    path("signup/",sign_view,name="signup"),
    path("logup/",log_view,name="logup"),
    path("myprof/",profile_view,name="myprof"),
    path("leaveapprov/",leaveapprove_view,name="leaveapprov")
]
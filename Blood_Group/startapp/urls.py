# pages/urls.py
from django.urls import path
from .views import homePageView,form,display


urlpatterns = [
    path("page/", homePageView, name="home"),
    path("form/",form,name="form"),
    path("display/",display,name="display")
]
from django.urls import path
from .views import load_page,add_page

urlpatterns = [
     path("index/", load_page, name="index"),
      path("sum/", add_page, name="sum")
]
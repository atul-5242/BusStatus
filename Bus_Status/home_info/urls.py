from django.contrib import admin
from django.urls import path
# from home_info import views line 3 and 4 Are same 
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('search/',views.search_,name="search")
]

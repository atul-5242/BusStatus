from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("",views.info,name="info"),
    path("info_bus/",views.info_bus,name="info_bus")
]

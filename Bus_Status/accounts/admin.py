from django.contrib import admin
from accounts.models import UserRegistration

class Student_User(admin.ModelAdmin):
    list_display=('id_here','username','email','password1','password2')
    
admin.site.register(UserRegistration,Student_User)
# Register your models here.
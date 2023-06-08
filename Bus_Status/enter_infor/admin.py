from django.contrib import admin
from enter_infor.models import Bus_infor

class Bus_information(admin.ModelAdmin):
    display_it=('Location','Time','Bus_no')
    
admin.site.register(Bus_infor,Bus_information)

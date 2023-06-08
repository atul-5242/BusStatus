from django.shortcuts import render,HttpResponse,redirect
from enter_infor.models import Bus_infor
# Create your views here.
def info(request):
    return render(request,"enter_info/for_entring_information.html")

def info_bus(request):
    if request.method=="POST":
        Location=request.POST.get("Location")
        Time=request.POST.get("Time")
        Bus_no=request.POST.get("Bus_no")
        value=Bus_infor(Location=Location,Time=Time,Bus_no=Bus_no)
        value.save()
        return HttpResponse("H")
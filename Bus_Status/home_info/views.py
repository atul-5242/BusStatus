from django.shortcuts import render,redirect
# from django.db.models import Q
from home_info.models import search
from django.http import HttpResponse,HttpResponseRedirect
from enter_infor.models import Bus_infor
# Create your views here.
def home(request):
    return render(request,"home/Homepage.html")

def search_(request):

    location=request.GET['Location']
    time=request.GET['Time']
    # # query=request.GET['query']
    # data_to_show=Bus_infor.objects.filter(Location=location,Time=time)
    # location=request.POST.get("Location")
    # time=request.POST.get("Time")
    # query=request.GET['query']
    # location=request.POST.get("Location")
    # time=request.POST.get("Time")
    # print(query)
    print(location,time)
    
    data_to_show=Bus_infor.objects.filter(Location__icontains=location,Time__icontains=time)
    # data_to_show=search.objects.filter(Location=location,Time=time)


# data_to_show=search.objects.filter(Location=location,Time=time)

# print(data_to_show)

    return render(request,"home/Search.html",{'data':data_to_show})


    
    
    
    
    # search_h=request.POST["search"]
    # # Time=request.POST.get("Time")
    # print(search_h)
    # all_bus_no=search.objects.filter(Location__icontains=search_h)
    # The_Time=search.objects.filter(Time__icontains=search_h)
    # all_query=all_bus_no.union(The_Time)
    # print(all_query)
    # dictionary={'all_query':all_query}
    # return render(request,'home/Homepage.html',dictionary)
    # return render(request,'home/Homepage.html',dictionary)
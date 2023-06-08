from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import UserRegistration

# Create your views here.
def login_page(request):
    return render(request,"accounts/login.html")
def signup_page(request):
    return render(request,"accounts/signup.html")


# def login_user(request):
#     if request.method == 'POST':
#         id_here = request.POST.get('id_here')
#         password = request.POST.get('password')
#         user = authenticate(id_here=id_here, password=password)
#         print(user)
#         if user is not None:
#             login(request, user)
#             redirect_url = request.GET.get('next', 'home')#at the place of next we can write o or Anything.
#             print(redirect_url)
#             return redirect(redirect_url)
#         else:
#             messages.error(request, "id_here Or Password is incorrect!",
#                            extra_tags='alert alert-warning alert-dismissible fade show')

#     return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


# def signup_user(request):
#     if request.method == 'POST':
#         check1 = False
#         check2 = False
#         check3 = False
#         # form = UserRegistration(request.POST)
#         # if form.is_valid_here():
#         username=request.POST.get('username')
#         id_here = request.POST.get('id_here')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         email = request.POST.get('email')

#         if password1 != password2:
#             check1 = True
#             messages.error(request, 'Password did_here not match!',
#                             extra_tags='alert alert-warning alert-dismissible fade show')
#         if User.objects.filter(id_here=id_here).exists():
#             check2 = True
#             messages.error(request, 'id_here already exists!',
#                             extra_tags='alert alert-warning alert-dismissible fade show')
#         if User.objects.filter(email=email).exists():
#             check3 = True
#             messages.error(request, 'Email already registered!',
#                             extra_tags='alert alert-warning alert-dismissible fade show')

#         if check1 or check2 or check3:
#             messages.error(
#                 request, "Registration Failed!", extra_tags='alert alert-warning alert-dismissible fade show')
#             return redirect('accounts/signup')
#         else:
#             user = User.objects.create_user(id_here=id_here,username=username,
#                 email=email , password1=password1,password2=password2)
#             user.save()
#             messages.success(
#                 request, f'Thanks for registering {user.username}.', extra_tags='alert alert-success alert-dismissible fade show')
#             return redirect('accounts/login')
#     else:
#         form = UserRegistration()
#     return render(request, 'accounts/signup.html', {'form': form})


def login_user(request):
    if request.method=='POST':
        id_here = request.POST.get('id_here')
        password1 = request.POST.get('password1')
        print(password1)
        user=authenticate(username=id_here,password=password1)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("T")



def signup_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        id_here = request.POST.get('id_here')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        # errors:=
    
        
        myuser=User.objects.create_user(id_here,email,password1)
        myuser.first_name=username
        d={"name":username}
        myuser.last_name=id_here
        myuser.save()
        student_user=UserRegistration(id_here=id_here,username=username,email=email,password1=password1,password2=password2)
        student_user.save()
        return render(request,"accounts/login.html",d)

    else:
        return HttpResponse("Not Found - 404")
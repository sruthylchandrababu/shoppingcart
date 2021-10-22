from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password1=request.POST['password2']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user name exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=email, password=password)
                user.save();
        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invaild userid or password')
            return redirect('login')
    else:
        return  render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
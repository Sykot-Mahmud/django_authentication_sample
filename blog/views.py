from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.



def registerpage(request):
    form=CreateUserForm()

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"Account Created successfully for :"+user)

            return redirect('login')
    context={'form':form}
    return render(request,'register.html',context)

def loginpage(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')
            # return render(request, 'login.html', context)

    context={}
    return render(request,'login.html',context)

def logoutpage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    context={}
    return render(request, 'index.html',context)
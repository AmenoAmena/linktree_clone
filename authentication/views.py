from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('authentication:register')
        else:
            messages.error(request, 'Invalid username or password') 
    
    return render(request,"authentication/login.html")

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            link1 = form.cleaned_data['link1']
            link2 = form.cleaned_data['link2']
            link3 = form.cleaned_data['link3']
            link4 = form.cleaned_data['link4']
            return redirect('authentication:login')
    return render(request,"authentication/register.html",{
        'form':form
    })

def logout_view(request):
    logout(request)
    return redirect('authentication:login')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import CustomUser, Clinic, Hospital
from django.contrib import messages
# Create your views here.


# Login View

def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, "email OR Password is incorrect")
        return render(request, 'authentication/login_form.html')


#  Logout View
@login_required(login_url = 'authentication:login')
def logoutView(request):
    if not request.user.is_authenticated:
        return redirect('authentication:login')
    else:
        logout(request)
        return redirect("/")


# Register View
def registerView(request):
    form = RegistrationForm()
    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    #     form = RegistrationForm()
    #     if request.method == "POST":
    #         form = RegistrationForm(request.POST):
    #         if form.is_valid():
    context = {
        'form':form
    }
    return render(request, 'authentication/register_form.html', context)
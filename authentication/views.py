from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ClinicInfoForm, HospitalInfoForm
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
#@login_required(login_url = 'authentication:login')
def registerView(request, role):
    
    if request.user.is_authenticated:
        return redirect('/')
    else:
        user_form = RegistrationForm()
        if role == "clinic":
            info_form = ClinicInfoForm()
        else:
            info_form = HospitalInfoForm()

        if request.method == "POST":
            user_form = RegistrationForm(request.POST)
            if role == "clinic":
                info_form = ClinicInfoForm(request.POST)
            else:
                info_form = HospitalInfoForm(request.POST)
            if user_form.is_valid() and info_form.is_valid():
                user = user_form.save(commit=False)
                user.role = role
                user.save()

                info = info_form.save(commit=False)
                info.user = user
                info.save()

                messages.success(request, 'Account was created Successfully')

                return redirect('authentication:login')

    context = {
        'user_form':user_form,
        'info_form':info_form,
    }
    return render(request, 'authentication/register_form.html', context)
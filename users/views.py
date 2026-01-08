from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomRegisterationForm
from django.contrib import messages
from django.contrib.auth import logout, login

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = CustomRegisterationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, "User created and logged in!")
            return redirect("homepage")
    else:
        register_form = CustomRegisterationForm()
    
    return render(request, "register.html", {"register_form": register_form})

def logout_view(request):
    logout(request)
    messages.success(request, "User Logged out Successfully!")
    return redirect('login')
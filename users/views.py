from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomRegisterationForm
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = CustomRegisterationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "User created!")
            return redirect("homepage")
    else:
        register_form = CustomRegisterationForm()
    
    return render(request, "register.html", {"register_form": register_form})

def logout_view(request):
    logout(request)
    messages.success(request, "User Logged out Successfully!")
    return redirect('login')
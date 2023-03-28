from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import RegistrationForm

# This is similar to what was done on the last project
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegistrationForm()
    return render(request, "profiles/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, 'profiles/profile.html')

#this function does not work for some reason
def logout_view(request):
    logout(request)
    return redirect('register') 
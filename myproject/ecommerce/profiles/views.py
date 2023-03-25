from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import RegistrationForm


# Most of this is built in django taken from my last project
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

def logout_view(request):
    logout(request)
    return redirect('register') 
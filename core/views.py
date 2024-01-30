from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, UpdateProfileForm


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("blogapp:index")
    return render(request, "core/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("blogapp:index")
        else:
            messages.warning(request, "Invalid credentials")
            return redirect("core:login")

    return render(request, "core/login.html")


@login_required(login_url="core:login")
def logout_view(request):
    logout(request)
    return redirect("core:login")


@login_required(login_url="core:login")
def profile(request):
    user = request.user
    return render(request, "core/profile.html", {"user": user})


@login_required(login_url="core:login")
def update_profile(request):
    user = request.user
    if user.is_authenticated:
        form = UpdateProfileForm(instance=user)
        if request.method == "POST":
            form = UpdateProfileForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully")
                return redirect("core:profile")
        return render(request, "core/update_profile.html", {"form": form})
    else:
        return redirect("core:update_profile")

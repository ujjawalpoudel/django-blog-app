from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    form = UserRegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        messages.success(request, f"Account created successfully for {username}!")
        return redirect("blog-home")

    # Handle errors efficiently
    if request.method == "POST":
        if User.objects.filter(username=request.POST.get("username", "")).exists():
            messages.error(
                request,
                "This username is already taken. Please choose a different one.",
            )
        elif request.POST.get("password1") != request.POST.get("password2"):
            messages.error(
                request,
                "Passwords do not match. Please enter the same password in both fields.",
            )
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

    return render(request, "users/register.html", {"form": form})

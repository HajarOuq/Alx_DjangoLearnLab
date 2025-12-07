from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, ProfileForm

# Registration view
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            return redirect("home")  # use named URL 'home' or change to '/'
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})

# Profile view (view and edit)
@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, "registration/profile.html", {"form": form, "success": True})
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "registration/profile.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm


def profiles(request):
    profiles_ = Profile.objects.all()
    return render(request, "profiles/profiles.html", {"profiles": profiles_})


def profile(request, pk):
    profile_ = Profile.objects.get(id=pk)
    return render(request, "profiles/profile.html", {"profile": profile_})


def LoginPage(request):
    context = {"page": "login"}
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You successfully logged in")
            return redirect('profiles')
        else:
            messages.error(request, "username or password is incorrect")
    return render(request, 'profiles/login_register.html', context)


def logoutPage(request):
    logout(request)

    return redirect('login')


def registerPage(request):
    form = CustomUserCreationForm(request.POST)
    context = {"page": "re gister", "form": form}
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "You succesfully registered")
            login(request, user)
            return redirect('profiles')
    return render(request, 'profiles/login_register.html', context)


def userAccaunt(request):
    context = {}
    return render(request, "profiles/accaunt.html", context)

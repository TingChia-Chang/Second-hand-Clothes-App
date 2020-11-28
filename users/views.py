from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.

def profile(request, username):
    user1 = get_object_or_404(User, username=username)
    return render(request,"users/user/profile.html", {"user": user1})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        messages.add_message(request, messages.SUCCESS, "You successfully registerd with the username: %s" % user.username)

        return redirect('second_hand_clothes_app:clothes_index')
    else:
        return render(request,"users/user/register.html",)

def login_user(request):
    username = request.POST.get("username")
    pw = request.POST.get("password")

    user = authenticate(username=username, password=pw)
    if user is not None:
        request.session['username'] = user.username
        request.session['role'] = user.detail.role
        messages.add_message(request, messages.SUCCESS, "You have logged in successfully.")
    else:
        messages.add_message(request, messages.ERROR, "Invalid username or password.")

    return redirect('second_hand_clothes_app:clothes_list')


def logout_user(request):
    del request.session['username']
    del request.session['role']
    return redirect('second_hand_clothes_app:clothes_index')

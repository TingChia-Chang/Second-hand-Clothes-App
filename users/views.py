from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from actions.models import Action
# Create your views here.

def profile(request, username):
    user1 = get_object_or_404(User, username=username)
    actions = Action.objects.all().filter(user=user1).order_by('-created_time')
    return render(request,"users/user/profile.html", {"user": user1, "actions":actions})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        last_name = request.POST.get('lastname')
        first_name = request.POST.get('firstname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password, last_name=last_name, first_name=first_name)
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

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from actions.models import Action
from users.models import Detail
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
        sex = request.POST.get('sex')

        user = User.objects.create_user(username, email, password, last_name=last_name, first_name=first_name)
        detail = Detail.objects.get(user_id=user.id)
        detail.sex = sex
        detail.save()
        messages.add_message(request, messages.SUCCESS, "You successfully registerd with the username: %s" % user.username)

        return redirect('second_hand_clothes_app:clothes_index')
    else:
        return render(request,"users/user/register.html",)

def edit_profile(request, username):
    if request.method == 'POST':
        last_name = request.POST.get('lastname')
        first_name = request.POST.get('firstname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        sex = request.POST.get('sex')

        try:
            user = get_object_or_404(User, username=username)
            detail = Detail.objects.get(user_id=user.id)
            user.last_name = last_name
            user.first_name = first_name
            user.email = email
            user.password = password
            if request.POST.get('role'):
                detail.role = request.POST.get('role')
                request.session['role'] = user.detail.role
            detail.sex = sex
            detail.save()
            user.save()

            action = Action(
                user = user,
                verb = "edit the profile",
                target = user,
            )
            action.save()

            messages.add_message(request, messages.INFO, "You successfully edited the profile")
            return redirect('users:profile', user.username)
        except User.DoesNotExist:
            return redirect('users:profile', user.username)
    else:
        user1 = get_object_or_404(User, username=username)
        detail1 = Detail.objects.get(user_id=user1.id)
        print(detail1.sex)
        return render(request, "users/user/edit_profile.html", {"user": user1})

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



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

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

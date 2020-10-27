from django.shortcuts import render, redirect
from .models import regular_user, admin_user, ClothesList

# Create your views here.
def clothes_index(request):
    clothes = ClothesList.objects.all()
    return render(request,"second_hand_clothes_app/clothes/index.html", {'clothes': clothes})

def clothes_list(request):
    clothes = ClothesList.objects.all()
    for i in clothes:
        print(i.picture.url)
    
    context = {'clothes': clothes}
    return render(request,"second_hand_clothes_app/clothes/list.html", context) 

def clothes_detail(request, item_id):
    clothes = ClothesList.objects.all()
    for clothes_item in clothes:
        if clothes_item.id == item_id:
            break
    return render(request,"second_hand_clothes_app/clothes/detail.html", {"clothes_item":clothes_item}) 

def clothes_add_item(request):
    return render(request,"second_hand_clothes_app/clothes/add_item.html")

def clothes_edit(request):
    return render(request,"second_hand_clothes_app/clothes/edit.html")

def clothes_search_result(request):
    return render(request,"second_hand_clothes_app/clothes/search-results.html")

def clothes_sign_in(request):
    return render(request,"second_hand_clothes_app/clothes/sign_in.html")

def sign_in(request):
    username = request.POST.get("username")
    print(username)
    pw = request.POST.get("password")
    print(pw)
    if (username == regular_user['username']) and (pw == regular_user['password']):
        request.session['username'] = username
        request.session['role'] = 'regular'
        return redirect('second_hand_clothes_app:clothes_list')
    elif (username == admin_user['username']) and (pw == admin_user['password']):
        request.session['username'] = username
        request.session['role'] = 'admin'
        return redirect('second_hand_clothes_app:clothes_list')
    else:
        return redirect('second_hand_clothes_app:clothes_index')

def log_out(request):
    del request.session['username']
    del request.session['role']
    return redirect('second_hand_clothes_app:clothes_index')
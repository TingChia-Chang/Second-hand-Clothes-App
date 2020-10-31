from django.shortcuts import render, redirect
from .models import regular_user, admin_user, ClothesList
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
def clothes_index(request):
    clothes = ClothesList.objects.all()
    return render(request,"second_hand_clothes_app/clothes/index.html", {'clothes': clothes})

def clothes_list(request):
    clothes = ClothesList.objects.all()
    
    context = {'clothes': clothes}
    return render(request,"second_hand_clothes_app/clothes/list.html", context) 

def clothes_sort(request):
    clothes = ClothesList.objects.all().order_by('price')
    
    context = {'clothes': clothes, 'order_by': 'price'}
    return render(request,"second_hand_clothes_app/clothes/list.html", context) 

def clothes_detail(request, item_id):
    clothes = ClothesList.objects.all()
    for clothes_item in clothes:
        if clothes_item.id == item_id:
            break
    return render(request,"second_hand_clothes_app/clothes/detail.html", {"clothes_item":clothes_item}) 

def clothes_add_item(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.FILES.get('image')
        size = request.POST.get('size')
        price = request.POST.get('price')
        des = request.POST.get('description')

        cl = ClothesList(
            name = name,
            seller = request.session.get('username'),
            picture = picture,
            size = size,
            price = price,
            description = des,
            comment = []
        )
        cl.save()
        messages.add_message(request, messages.SUCCESS, "You successfully submitted the clothes: %s" % cl.name)
        return redirect('second_hand_clothes_app:clothes_detail', cl.id)
    else:
        return render(request,"second_hand_clothes_app/clothes/add_item.html")

def clothes_edit(request, item_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.FILES.get('image')
        size = request.POST.get('size')
        price = request.POST.get('price')
        des = request.POST.get('description')

        try:
            clothes = ClothesList.objects.get(pk=item_id)
            clothes.name = name
            clothes.size = size
            clothes.price = price
            clothes.description = des
            if picture:
                clothes.picture = picture
            clothes.save()
            messages.add_message(request, messages.INFO, "You successfully edited the clothes: %s" % clothes.name)
            return redirect('second_hand_clothes_app:clothes_detail', clothes.id)
        except ClothesList.DoesNotExist:
            return redirect('second_hand_clothes_app:clothes_index')
    else:
        clothes = ClothesList.objects.all()
        for item in clothes:
            if item.id == item_id:
                break
        return render(request,"second_hand_clothes_app/clothes/edit.html", {"item": item})

def clothes_delete(request, item_id):
    clothes = ClothesList.objects.get(pk=item_id)
    ClothesList.objects.get(pk=item_id).delete()
    messages.add_message(request, messages.WARNING, "You successfully deleted the clothes: %s" % clothes.name)
    return redirect('second_hand_clothes_app:clothes_list')



def clothes_show_comment(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        clothes_id = request.POST.get('clothes_id')
        try:
            clothes = ClothesList.objects.get(pk=clothes_id)


            return JsonResponse({'success': 'success', 'comment': clothes.comment}, status=200)
        except ClothesList.DoesNotExist:
            return JsonResponse({'error': 'No clothes found with that ID'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid Ajax request'}, status=400)

def clothes_add_comment(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        clothes_id = request.POST.get('clothes_id')
        clothes_comment = request.POST.get('clothes_comment')
        if clothes_comment != "":
            comment = request.session.get("username") + ":" + clothes_comment
            try:
                clothes = ClothesList.objects.get(pk=clothes_id)
                clothes.comment.append(comment)
                clothes.save()

                return JsonResponse({'success': 'success', 'comment': comment}, status=200)
            except ClothesList.DoesNotExist:
                return JsonResponse({'error': 'No clothes found with that ID'}, status=200)
        else:
            return JsonResponse({'error': 'No comment'}, status=200)    
    else:
        return JsonResponse({'error': 'Invalid Ajax request'}, status=400)


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
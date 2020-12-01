from django.shortcuts import render, redirect
from .models import regular_user, admin_user, ClothesList, User
from django.http import JsonResponse
from django.contrib import messages
from actions.models import Action
from comments.models import Comment
from django.core import serializers
from django.urls import reverse
from django.contrib.humanize.templatetags.humanize import naturaltime

# Create your views here.
def clothes_index(request):
    clothes = ClothesList.objects.all()
    actions = Action.objects.all().order_by('-created_time')
    return render(request,"second_hand_clothes_app/clothes/index.html", {'clothes': clothes, 'actions':actions})

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
    user = User.objects.get(username=clothes_item.seller)
    username = request.session.get("username")
    comments = Comment.objects.all().filter(user_id=user.id).order_by('-created_time')
    return render(request,"second_hand_clothes_app/clothes/detail.html", {"clothes_item":clothes_item, "comments":comments}) 

def clothes_add_item(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.FILES.get('image')
        size = request.POST.get('size')
        price = request.POST.get('price')
        des = request.POST.get('description')

        user = User.objects.get(username=request.session.get("username"))

        cl = ClothesList(
            name = name,
            seller = request.session.get('username'),
            picture = picture,
            size = size,
            price = price,
            description = des,
            comment = [],
            user=user,
        )
        cl.save()

        #log the action
        action = Action(
            user = user,
            verb = "create the item",
            target = cl,
        )
        action.save()

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
        user = User.objects.get(username=request.session.get("username"))

        try:
            clothes = ClothesList.objects.get(pk=item_id)
            clothes.name = name
            clothes.size = size
            clothes.price = price
            clothes.description = des
            if picture:
                clothes.picture = picture
            clothes.save()

            #log the action
            action = Action(
                user = user,
                verb = "edit the item",
                target = clothes,
            )
            action.save()

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
    user = User.objects.get(username=request.session.get("username"))
    clothes = ClothesList.objects.get(pk=item_id)
    ClothesList.objects.get(pk=item_id).delete()
    action = Action(
        user = user,
        verb = "delete the item",
        target = clothes,
    )
    action.save()
    messages.add_message(request, messages.WARNING, "You successfully deleted the clothes: %s" % clothes.name)
    return redirect('second_hand_clothes_app:clothes_list')



# def clothes_show_comment(request):
#     is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
#     if is_ajax and request.method == "POST":
#         clothes_id = request.POST.get('clothes_id')
#         clothes = ClothesList.objects.get(pk=clothes_id)
        # user = User.objects.get(username=clothes.seller)
        # try:
        #     comments_json = serializers.serialize("json", Comment.objects.all().filter(user_id=user.id))
        #     username = request.session.get("username")
        #     url = reverse('users:profile', args=[username])

        #     return JsonResponse({'success': 'success', 'comment': comments_json, 'url': url}, status=200)
        # except ClothesList.DoesNotExist:
        #     return JsonResponse({'error': 'No clothes found with that ID'}, status=200)
#     else:
#         return JsonResponse({'error': 'Invalid Ajax request'}, status=400)

def clothes_add_comment(request):
    user1 = User.objects.get(username=request.session.get("username"))
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        clothes_id = request.POST.get('clothes_id')
        clothes_comment = request.POST.get('clothes_comment')
        clothes = ClothesList.objects.get(pk=clothes_id)
        user = User.objects.get(username=clothes.seller)
        if clothes_comment != "":
            try:
                # clothes = ClothesList.objects.get(pk=clothes_id)
                cm = Comment(
                    user = user,
                    comment = clothes_comment,
                    username = request.session.get("username"),
                )
                cm.save()

                action = Action(
                    user = user1,
                    verb = "add a comment to the item",
                    target = clothes,
                )
                action.save()
                url = reverse('users:profile', args=[request.session.get("username")])
                time = naturaltime(cm.created_time)

                return JsonResponse({'success': 'success', 'comment': clothes_comment, 'url': url, 'username': request.session.get("username"), 'time':time}, status=200)
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


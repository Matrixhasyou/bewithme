from django.shortcuts import render, redirect
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from .models import User, Question, FavoriteItems, run_init, Notification, how_often_to_days, days_to_how_often
import random
import datetime
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'user/index.html')

@csrf_exempt
def post_check(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        return HttpResponse(data)
    else:
        return HttpResponse("Hello")

def init(request):
    run_init()
    return HttpResponse("DONE!")

def notification_delete(request):
    Notification.objects.all().delete()
    return HttpResponse("DONE!")

@csrf_exempt
def auth(request):
    if request.method == 'POST':
        try:
            check_user = User.objects.get(email = request.POST.get("email", ""))
        except User.DoesNotExist:
            return render(request, 'user/auth.html')
        if request.POST.get("password", "") == check_user.password:
            return redirect("question_list", check_user.id) # in page
        else: return render(request, 'user/auth.html')
    else:
        return render(request, 'user/auth.html')

def question_list(request, id_page):
    user = User.objects.get(id=id_page)
    q = Question.objects.all()
    return render(request, "user/questionary.html", {"user": user,
                                                     "question": q,})

def partners_likes(request, id_page):
    user = User.objects.get(id=id_page)
    f = FavoriteItems.objects.filter(user_id = user.relation)
    return render(request, "user/fav.html", {"user": user,
                                             "fav": f,})
@csrf_exempt
def jauth(request):
    data = {}
    if request.method == 'POST':
        try:
            check_user = User.objects.get(email = request.POST.get("email", ""))
        except User.DoesNotExist:
            data['invalid_data'] = "Wrong email or password"
            return JsonResponse(data)
        if request.POST.get("password", "") == check_user.password:
            data["user_id"] = check_user.id
            return JsonResponse(data)
        else: return JsonResponse(data)
    else:
        return JsonResponse(data)

def jprofile(self, id_user):
    user = User.objects.get(id=id_user)
    return JsonResponse(user.get_dict() , safe=False)

@csrf_exempt
def jquestion_list(request, id_user):
    if request.method == 'POST':
        fav_id = request.POST.get("question_id", "")
        fav_item = FavoriteItems.objects.get(id=fav_id)
        fav_item.options = request.POST.get("f_options", "")
        #fav_item.save()
        return JsonResponse({})
    else:
        data = []
        for fav_item in FavoriteItems.objects.filter(user_id=id_user):
            data.append(fav_item.get_dict_first(),)
        return JsonResponse(data, safe=False)

@csrf_exempt
def jpartners_likes(request, id_user):
    if request.method == "POST":
        fav_item = FavoriteItems.objects.get(id=request.POST.get("favoriteitem_id", ""))
        #if request.POST.get("last_date", "") != '':
        fav_item.f_last_date = request.POST.get("last_date", "")
        fav_item.how_often = how_often_to_days(request.POST.get("how_often", ""))
        fav_item.save()
        return JsonResponse({})
    else:
        rel = User.objects.get(id=id_user).relation
        data = []
        partner_name = User.objects.get(id=rel).firstname
        fav_items = FavoriteItems.objects.filter(user_id = rel)
        for f in fav_items:
            data.append(f.get_dict_second(partner_name))
        return JsonResponse(data, safe=False)

def jget_reminders_list(request, id_user): # 1 alice
    data = []
    generate_reminders(id_user)#alice
    notifications = Notification.objects.filter(user_id=id_user)
    for n in notifications:
        data.append(n.get_dict())
    return JsonResponse(data, safe=False)

def generate_reminders(id_user):#a
    user = User.objects.get(id=id_user)
    parner_user = User.objects.get(id=user.relation)
    fav_items = FavoriteItems.objects.filter(user_id=user.relation)#a
    for fav_item in fav_items: #all alice fav
        need_to_create_notification = True
        try:
            notifications = Notification.objects.filter(favorite_id=fav_item.id)#if fav has notif many
            for notification in notifications: #every notification
                if  not notification.done:
                    need_to_create_notification = False
        except: pass
        if need_to_create_notification and fav_item.how_often != 0:
            n = Notification(user_id = id_user,
                             favorite_id = fav_item.id,
                             start_date = fav_item.f_last_date + datetime.timedelta(days=fav_item.how_often),
                             notification_text = fav_item.notification_text.replace('{PARTNERSNAME}', parner_user.firstname).replace('{ITEM}', random.choice(fav_item.f_options.split(','))),
                             done = False,)
            n.save()

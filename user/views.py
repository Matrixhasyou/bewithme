from django.shortcuts import render, redirect
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from .models import User, Question, FavoriteItems, run_init, Notification

def init(request):
    run_init()
    return "DONE!"

def auth(request):
    if request.method == 'POST':
        try:
            check_user = User.objects.get(email = request.POST.get("email", ""))
        except User.DoesNotExist:
            return render(request, 'user/auth.html')
        if request.POST.get("password", "") == check_user.password:
            return redirect("inin", check_user.id) # in page
        else: return render(request, 'user/auth.html')
    else:
        return render(request, 'user/auth.html')

def q_page(request, id_page):
    user = User.objects.get(id=id_page)
    q = Question.objects.all()
    return render(request, "user/questionary.html", {"user": user,
                                                     "question": q,
                                                        })

def a_page(request, id_page):
    user = User.objects.get(id=id_page)
    f = FavoriteItems.objects.filter(user_id = user.relation)
    return render(request, "user/fav.html", {"user": user,
                                                     "fav": f,
                                                      })

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

def profile(request, id_user):
    if request.method == 'POST':
        fav_id = request.fav_id
        f = FavoriteItems.objects.get(id=fav_id)
        f.options = request.options
        f.save()
        return 'OK'
    else:
        user = User.objects.get(id=id_user)
        data = {

        }
        for obj in FavoriteItems.objects.all():
            data.append(obj.get_dict_first(),)
        return JsonResponse(data, safe=False)

def jpartners_likes(request, id_user):
    rel = User.objects.get(id=id_user).relation
    data = []
    partner_name = User.objects.get(id=rel).firstname
    fav_items = FavoriteItems.objects.filter(user_id = rel)
    for f in fav_items:
        data.append(f.get_dict_second(partner_name))
    return JsonResponse(data, safe=False)

def get_reminders_list(request):
    reminders_list = Notification.objects.all()
    data = []
    #generate_reminders()

    return JsonResponse(data, safe=False)

'''def generate_reminders():

        fav_item = FavoriteItems.objects.all()
        text = ''
        name = User.objects.get(id=fav_item.user_id).firstname
        for item in fav_items:
            name = User.objects.get(id=fav_item.user_id).firstname
            date = fav_item.f_last_date + datetime.timedelta(days=fav_item.how_often)
            item.notification_text = 'jkhygjygkjgy'






            data = {'date_to_notify': fav_item.f_last_date + datetime.timedelta(days=fav_item.how_often)}
            if fav_item.f_item == "cuisine":
                text = "Time to take " + name + " eat some " + random.choice(fav_item.f_options.split(',')) + " cuisine"
            elif fav_item.f_item == "flowers":
                text = "Time to get " + name + " a cute bunch of " + random.choice(fav_item.f_options.split(','))
            elif fav_item.f_item == "go_out":
                text = "It's time that you and " + name + " went " + random.choice(fav_item.f_options.split(','))
            elif fav_item.f_item == "vacation":
                text = "Vacation time! You know what would be great? " + random.choice(fav_item.f_options.split(',')).capitalize()
            elif fav_item.f_item == "music":
                text = "It's a long time since you and " + name + " shared " + random.choice(fav_item.f_options.split(',')


        return JsonResponse({'text': text})

        def get_dict(self):'''

from django.db import models
import random
import datetime

URL_GETTER = { "roses" : "static/img/Roses.png",
                "white lilies" : "static/img/WhiteLilies.png",
                "tulips" : "static/img/Tulips.png",
                "sunflowers" : "static/img/Sunflower.png",

                "Italian cuisine" : "static/img/Italian.png",
                "Greek cuisine" : "static/img/Greek.png",
                "French cuisine" : "static/img/French.png",
                "Thai cuisine" : "static/img/Chenese.png"
}

def run_init():
    U1 = User(firstname="Alice",
                lastname="Cooper",
                email="a@a.com",
                password="alice",
                gender="female",
                relation="2",     )
    U1.save()
    U2 = User(firstname="Bob",
                lastname="Dylan",
                email="b@a.com",
                password="bob",
                gender="male",
                relation="1",)

    U2.save()

    Q1 = Question(question_text = 'What are your favorite flowers?',
                 q_item = "flowers",
                 q_options_list = "roses,white lilies,tulips,sunflowers",
                 q_last = "When did you last give {PARTNERSNAME}",
                 notification_text="Time to get {PARTNERSNAME} a cute bunch of {ITEM}", #to dict
                 img_url = "")
    Q1.save()

    Q2 = Question(question_text = 'What is your favorite cuisine?',
                 q_item = "cusine",
                 q_options_list = "Italian cuisine,Thai cuisine,French cuisine,Greek cuisine",
                 q_last = "When did you last take {PARTNERSNAME} to try {ITEM}",
                 notification_text="Time to take {PARTNERSNAME} to eat some {ITEM}", #to dict
                 img_url = "")

    Q2.save()

    F1 = FavoriteItems(question_text = 'What are your favorite flowers?',
                      f_options_list = "roses,white lilies,tulips,sunflowers",
                      user_id = 1,
                      f_item = "flowers",
                      f_options = "roses",
                      f_last_q = "When did you las give {PARTNERSNAME}",
                      f_last_date = datetime.datetime.now()-datetime.timedelta(days=60),
                      how_often = 60,
                      notification_text="Time to get {PARTNERSNAME} a cute bunch of {ITEM}",
                      img_url = "")


    F1.save()
    F2 = FavoriteItems(question_text = 'What is your favorite cuisine?',
                      f_options_list = "Italian cuisine,Thai cuisine,French cuisine,Greek cuisine",
                      user_id = 1,
                      f_item = "cusine",
                      f_options = "Italian cuisine,Thai cuisine",
                      f_last_q = "When did you last take {PARTNERSNAME} to try {ITEM}",
                      f_last_date = datetime.datetime.now()-datetime.timedelta(days=31),
                      how_often = 30,
                      notification_text="Time to take {PARTNERSNAME} to eat some {ITEM}",
                      img_url = "")
    F2.save()

    return 'Done!'

def get_option_url(some_list):
    url = {}
    options = some_list.split(',')
    for o in options:
        url[o] = URL_GETTER[o]
    return url

def how_often_to_days(how_often):
    string = how_often.split(' ')
    if string[-1] == "week":
        return 7
    elif string[-1] == "month":
        return 30
    elif string[-1] == "months":
        return int(string[-2])*30
    elif string[-1] == "year":
        return 365
    elif string[-1] == 'chosen':
        return 0
    else:
        return 7

def days_to_how_often(days):
    if days / 365 >= 1:
        return 'every year'
    elif days / 30 >= 1:
        return 'every '+ str(days // 30) + ' months'
    elif days / 7 <=1 :
        return 'every week'
    elif days == 0:
        return 'Not chosen'
    else:
        return 'every week'

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    relation = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.email

    def get_dict(self):
        data = {
        'user_id' : self.id,
        'firstname' : self.firstname,
        'lastname' : self.lastname,
        'email' : self.email,
        'gender' : self.gender,
        }
        return data


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    q_item = models.CharField(max_length=200, default="null")
    q_options_list = models.CharField(max_length=500, default="null")
    q_options_selected = models.CharField(max_length=500, default="", blank=True)
    q_last = models.CharField(max_length=200, default="null")
    notification_text = models.CharField(max_length=200, default="null")
    img_url = models.CharField(max_length=200, default="null")

    def __str__(self):
        return self.question_text

    def get_dict(self):
        data = { 'question_text' : self.question_text,
                 'q_options_list' : get_option_url(self.q_options_list),
                 'q_options_selected' : get_option_url(self.q_options_selected),
                 'q_item' : self.q_item,}
        return data

class Notification(models.Model):
    user_id = models.IntegerField(default=0, null=True)
    favorite_id = models.IntegerField(default=0, null=True)
    start_date = models.DateField(null=True, default=None)
    notification_text = models.CharField(max_length=500, default="", blank=True)
    done = models.BooleanField(default=False)

    def get_dict(self):
        data = {
            'user_id' : self.user_id,
            'favorite_id' : self.favorite_id,
            'start_date' : self.start_date,
            'notifications_text' : self.notification_text,#
            'done' : self.done, }
        return data

class FavoriteItems(models.Model):
    question_text = models.CharField(max_length=200, default="null")
    user_id = models.IntegerField(default=0, null=True)
    f_item = models.CharField(max_length=200, default="null")
    f_options_list = models.CharField(max_length=500, default="null")
    f_options = models.CharField(max_length=500, default="")
    f_last_q = models.CharField(max_length=200, default="null")
    f_last_date = models.DateField(null=True, default=None)
    how_often = models.IntegerField(default=0, null=True)
    notification_text = models.CharField(max_length=200, default="null")
    img_url = models.CharField(max_length=200, default="null")

    def get_question(self):
        return self.f_last_q.replace("{ITEM}", self.f_item)+'?'


    def get_dict_first(self):
        data = { 'question_text' : self.question_text,
                 'f_options_list' : get_option_url(self.f_options_list),
                 'f_options' : get_option_url(self.f_options),
                 'question_id' : self.id,
                 'img_url': self.img_url,
                  }
        return data

    def get_dict_second(self, name):
        data = {'last_question': self.f_last_q.replace('{PARTNERSNAME}', name)+' '+random.choice(self.f_options.split(','))+'?',
                'last_date': self.f_last_date,
                'reminder' : "How often to remind you to do this?",
                'how_often' : days_to_how_often(self.how_often),
                'f_options' : get_option_url(self.f_options),
                'favoriteitem_id' : self.id,
                'img_url': self.img_url,

            }
        return data

from django.db import models
import random
import datetime

def run_init():
    Q = Question(question_text = 'What are your favorite flowers?',
                 q_item = "flowers",
                 q_options_list = "roses/daisys/tulips",
                 q_last = "When did you las give {PARTNERSNAME}",)
    Q.save()
    F = FavoriteItems(question_text = 'What are your favorite flowers?',
                      f_options_list = "roses/daisys/tulips",
                      user_id = 1,
                      f_item = "flowers",
                      f_options = "roses",
                      f_last_q = "When did you las give {PARTNERSNAME}",
                      f_last_date = None,
                      how_often = 60,)
    F.save()


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
        'firstname' : self.firstname,
        'lastname' : self.lastname,
        'email' : self.email,
        'password' : self.password,
        'gender' : self.password,
        'relation' : self.relation,
        }
        return data


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    q_item = models.CharField(max_length=200, default="null")
    q_options_list = models.CharField(max_length=500, default="null")
    q_options_selected = models.CharField(max_length=500, default="", blank=True)
    q_last = models.CharField(max_length=200, default="null")

    def __str__(self):
        return self.question_text

    def get_options(self):
        return self.q_options_list.split('/')

    def get_dict(self):
        data = { 'question_text' : self.question_text,
                 'q_options_list' : self.get_options(),
                 'q_item' : self.q_item,}
        return data

'''class Notification(models.Model):
    favorite_id = models.ForeignKey(FavoriteItems, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def generate(self):
        fav_item = FavoriteItems.objects.get(id=self.favorite_id)
        name = User.objects.get(id=User.object.get(relation=fav_item.user_id))
        data = {'date_to_notify': fav_item.f_last_date + datetime.timedelta(days=fav_item.how_often)}
        if fav_item.f_item == "cuisine":
            text = "Time to take " + name + " eat some " + random.choice(fav_item.f_options.split(',')) + " cuisine"

        data['text'] = text
        return data
'''

class FavoriteItems(models.Model):
    question_text = models.CharField(max_length=200, default="null")
    user_id = models.IntegerField(default=0, null=True)
    f_item = models.CharField(max_length=200, default="null")
    f_options_list = models.CharField(max_length=500, default="null")
    f_options = models.CharField(max_length=500, default="")
    f_last_q = models.CharField(max_length=200, default="null")
    f_last_date = models.DateField(null=True, default=None)
    how_often = models.IntegerField(default=0, null=True)

    def get_question(self):
        return self.f_last_q +" "+self.f_item+'?'

    def get_dict_first(self):
        data = { 'question_text' : self.question_text,
                 'f_options_list' : self.f_options_list.split(','),
                 'f_options' : self.f_options.split(','),
                 'question_id' : self.id,
                 }
        return data

    def remind_to_days(self, remind):
        string = remind.split(' ')
        if string[-1] == "week":
            return 7
        elif string[-1] == "month":
            return 30
        elif string[-1] == "months":
            return int(string[-2])*30

    def get_dict_second(self, name):
        data = {'last_question': self.f_last_q.replace('{PARTNERSNAME}', name)+' '+random.choice(self.f_options.split(','))+'.',
                'reminder' : "How often to remind you to do this?",
                'how_often' : self.how_often,
            }
        return data

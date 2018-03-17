from .models import Question, User, FavoriteItems
def run init():
    Q = Question(question_text = 'What are your favorite flowers?',
                 q_item = "flowers",
                 q_options_list = "roses/daisys/tulips",
                 q_last = "When did you las give {PARTNERSNAME}",)
    Q.save()

    F = FavoriteItems(question_text = 'What are your favorite flowers?',
                      q_item = "flowers",
                      q_options_list = "roses/daisys/tulips",
                      q_last = "When did you las give {PARTNERSNAME}",
                      user_id = 1,
                      f_item = "flowers",
                      f_options_list = "roses/daisys/tulips",
                      f_options = "roses",
                      f_last_q = "When did you las give {PARTNERSNAME}",
                      f_last_date = None,
                      how_often = 60,)
    f.save()

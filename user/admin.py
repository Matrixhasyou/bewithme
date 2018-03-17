from django.contrib import admin

from .models import Question, User, FavoriteItems, Notification

admin.site.register(User)
admin.site.register(Question)
admin.site.register(FavoriteItems)
admin.site.register(Notification)

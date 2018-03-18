"""BWM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
            path('admin', admin.site.urls),

            path('', views.index, name="index"),
            path('post', views.post_check, name="post"),
            path('del_notifications', views.notification_delete, name="notif"),
            path('init', views.init, name="init"),
            path('auth', views.auth, name="auth"),
            path('q_l/<int:id_page>', views.question_list, name="q_l"),
            path('p_l/<int:id_page>', views.partners_likes, name="p_l"),

            path('api/jauth', views.jauth, name="auth"),
            path('api/profile/<int:id_user>', views.jprofile, name="jprof"),
            path('api/question_list/<int:id_user>', views.jquestion_list, name="jq_l"),
            path('api/partners_likes/<int:id_user>', views.jpartners_likes, name="jp_l"),
            path('api/reminders_list/<int:id_user>', views.jget_reminders_list, name="jreminder"),]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

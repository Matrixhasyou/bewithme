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

urlpatterns = [
    path('init', views.init),
    path('admin/', admin.site.urls),
    path('auth/', views.auth, name="auth"),
    path('in/<int:id_page>', views.q_page, name="inin"),
    path('out/<int:id_page>', views.a_page, name="outout"),

    path('jauth', views.jauth, name="auth"),
    path('profile/<int:id_user>', views.profile, name="prof"),
    path('partners_likes/<int:id_user>', views.jpartners_likes, name="a"),
    path('reminders_list/', views.get_reminders_list, name="rem"),
]

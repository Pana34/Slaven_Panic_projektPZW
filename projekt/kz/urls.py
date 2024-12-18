from django.contrib import admin
from django.urls import path, include
from main import views
from main.views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')), 
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/register/', register, name='register'), 
    path('', views.index, name='index'),
    path('logout/', views.custom_logout, name='logout'),
]

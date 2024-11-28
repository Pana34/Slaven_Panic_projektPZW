from django.urls import path
from . import views

urlpatterns = [
    path('budzet/', views.budzet_list, name='budzet_list'),
    path('prihod/', views.prihod_list, name='prihod_list'),
    path('rashod/', views.rashod_list, name='rashod_list'),
    path('tag/', views.tag_list, name='tag_list'),
]

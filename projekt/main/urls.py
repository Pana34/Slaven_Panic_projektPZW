from django.urls import path
from . import views
from main.views import BudzetList, PrihodList, RashodList, TagList
from main.views import BudzetDetailView, PrihodDetailView, RashodDetailView, TagDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('korisnik/', views.korisnik, name='korisnik'),
    path('budzeti/', BudzetList.as_view(), name= 'budzet_list'),
    path('prihodi/', PrihodList.as_view(), name='prihod_list'),
    path('rashodi/', RashodList.as_view(), name='rashod_list'),
    path('kategorije/', TagList.as_view(), name='tag_list'),
    path('budzet/<str:naziv>/', BudzetDetailView.as_view(), name='budzet_detail'),
    path('prihod/<str:naziv>/', PrihodDetailView.as_view(), name='prihod_detail'),
    path('rashod/<str:naziv>/', RashodDetailView.as_view(), name='rashod_detail'),
    path('kategorija/<str:naziv>/', TagDetailView.as_view(), name='tag_detail'),

]

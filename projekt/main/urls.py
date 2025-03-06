from django.urls import path
from . import views
from main.views import BudzetList, PrihodList, RashodList, TagList
from main.views import BudzetDetailView, PrihodDetailView, RashodDetailView, TagDetailView
from main.views import BudzetCreateView, BudzetUpdateView, BudzetDeleteView
from main.views import PrihodCreateView, PrihodUpdateView, PrihodDeleteView
from main.views import RashodCreateView, RashodUpdateView, RashodDeleteView
from main.views import TagCreateView, TagUpdateView, TagDeleteView
from .views import BudzetListCreateAPIView, BudzetRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('', views.index, name='index'),
    path('api/budget_data/', views.budget_data, name='budget_data'),
    path('api/income_expense_data/', views.income_expense_data, name='income_expense_data'),
    path('api/financial_trend_data/', views.financial_trend_data, name='financial_trend_data'),
    path('korisnik/', views.korisnik, name='korisnik'),
    path('budzeti/', BudzetList.as_view(), name= 'budzet_list'),
    path('prihodi/', PrihodList.as_view(), name='prihod_list'),
    path('rashodi/', RashodList.as_view(), name='rashod_list'),
    path('kategorije/', TagList.as_view(), name='tag_list'),
    path('budzet/create/', BudzetCreateView.as_view(), name='budzet-create'),
    path('budzet/<str:naziv>/update/', BudzetUpdateView.as_view(), name='budzet-update'),
    path('budzet/<str:naziv>/delete/', BudzetDeleteView.as_view(), name='budzet-delete'),
    path('budzet/<str:naziv>/', BudzetDetailView.as_view(), name='budzet_detail'),
    path('prihod/create/', PrihodCreateView.as_view(), name='prihod-create'),
    path('prihod/<str:naziv>/update/', PrihodUpdateView.as_view(), name='prihod-update'),
    path('prihod/<str:naziv>/delete/', PrihodDeleteView.as_view(), name='prihod-delete'),
    path('prihod/<str:naziv>/', PrihodDetailView.as_view(), name='prihod_detail'),
    path('rashod/create/', RashodCreateView.as_view(), name='rashod-create'),
    path('rashod/<str:naziv>/update/', RashodUpdateView.as_view(), name='rashod-update'),
    path('rashod/<str:naziv>/delete/', RashodDeleteView.as_view(), name='rashod-delete'),
    path('rashod/<str:naziv>/', RashodDetailView.as_view(), name='rashod_detail'),
    path('kategorija/create/', TagCreateView.as_view(), name='kategorija-create'),
    path('kategorija/<str:naziv>/update/', TagUpdateView.as_view(), name='kategorija-update'),
    path('kategorija/<str:naziv>/delete/', TagDeleteView.as_view(), name='kategorija-delete'),
    path('kategorija/<str:naziv>/', TagDetailView.as_view(), name='tag_detail'),
    path('api/budzeti/', BudzetListCreateAPIView.as_view(), name='budzet-list-create'),
    path('api/budzeti/<str:naziv>/', BudzetRetrieveUpdateDestroyAPIView.as_view(), name='budzet-detail'),
]

from django.shortcuts import render, redirect
from .models import Budzet, Prihod, Rashod, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from django.views.generic import ListView
from main.models import Budzet, Prihod, Rashod, Tag
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.shortcuts import render

def index(request):
    is_admin = request.user.groups.filter(name="Administrator").exists()
    is_user = request.user.groups.filter(name="Korisnik").exists()
    
    context = {
        'is_admin': is_admin,
        'is_user': is_user,
    }
    
    return render(request, 'main/index.html', context)



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            korisnik_group = Group.objects.get(name='Korisnik') 
            user.groups.add(korisnik_group)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            if user is not None: 
                login(request, user)  
                return redirect('index')
            else:
                return render(request, 'registration/register.html', {
                    'form': form,
                    'error': 'Autentifikacija nije uspjela. Pokušajte ponovo.',
                })
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

#administrator
def is_admin(user):
    return user.groups.filter(name='Administrator').exists()

@user_passes_test(is_admin)
def admin_only_view(request):
    return render(request, 'admin.html')

#korisnik
def is_user(user):
    return user.groups.filter(name='Korisnik').exists()

@user_passes_test(is_user)
def user_only_view(request):
    return render(request, 'main/korisnik.html')

def korisnik(request):
    return render(request, 'main/korisnik.html')

def custom_logout(request):
    logout(request)
    return redirect('login')

def budzet_list(request):
    budzeti = Budzet.objects.all() 
    return render(request, 'main/budzet_list.html', {'budzeti': budzeti})

def prihod_list(request):
    prihodi = Prihod.objects.all()
    return render(request, 'main/prihod_list.html', {'prihodi': prihodi})

def rashod_list(request):
    rashodi = Rashod.objects.all()
    return render(request, 'main/rashod_list.html', {'rashodi': rashodi})

def tag_list(request):
    tagovi = Tag.objects.all()
    return render(request, 'main/tag_list.html', {'tagovi': tagovi})


class BudzetList(ListView):
    model = Budzet
    template_name = 'main/budzet_list.html' 
    context_object_name = 'budzeti'  

    def get_queryset(self):
        queryset = Budzet.objects.all()
        naziv_filter = self.request.GET.get('naziv')
        if naziv_filter:
            queryset = queryset.filter(naziv__icontains=naziv_filter)
        return queryset

class PrihodList(ListView):
    model = Prihod
    template_name = 'main/prihod_list.html'
    context_object_name = 'prihodi'

    def get_queryset(self):
        queryset = Prihod.objects.all()
        datum_od = self.request.GET.get('datum_od')
        datum_do = self.request.GET.get('datum_do')
        if datum_od:
            queryset = queryset.filter(datum__gte=datum_od)
        if datum_do:
            queryset = queryset.filter(datum__lte=datum_do)
        return queryset


class RashodList(ListView):
    model = Rashod
    template_name = 'main/rashod_list.html'
    context_object_name = 'rashodi'

    def get_queryset(self):
        queryset = Rashod.objects.all()
        datum_od = self.request.GET.get('datum_od')
        datum_do = self.request.GET.get('datum_do')
        if datum_od:
            queryset = queryset.filter(datum__gte=datum_od)
        if datum_do:
            queryset = queryset.filter(datum__lte=datum_do)
        return queryset


class TagList(ListView):
    model = Tag
    template_name = 'main/tag_list.html'
    context_object_name = 'kategorije'

    def get_queryset(self):
        queryset = Tag.objects.all()
        naziv_filter = self.request.GET.get('naziv')
        if naziv_filter:
            queryset = queryset.filter(naziv__icontains=naziv_filter)
        return queryset


class BudzetDetailView(DetailView):
    model = Budzet
    template_name = 'main/budzet_detail.html'
    context_object_name = 'budzet'

    def get_object(self):
        return get_object_or_404(Budzet, naziv=self.kwargs['naziv'])

class PrihodDetailView(DetailView):
    model = Prihod
    template_name = 'main/prihod_detail.html'
    context_object_name = 'prihod'

    def get_object(self):
        return get_object_or_404(Prihod, naziv=self.kwargs['naziv'])

class RashodDetailView(DetailView):
    model = Rashod
    template_name = 'main/rashod_detail.html'
    context_object_name = 'rashod'

    def get_object(self):
        return get_object_or_404(Rashod, naziv=self.kwargs['naziv'])

class TagDetailView(DetailView):
    model = Tag
    template_name = 'main/tag_detail.html'
    context_object_name = 'kategorija'

    def get_object(self):
        return get_object_or_404(Tag, naziv=self.kwargs['naziv'])
    
class BudzetCreateView(CreateView):
    model = Budzet
    fields = ['naziv', 'iznos', 'datum', 'opis', 'tag']
    template_name = 'main/budzet_form.html'
    success_url = reverse_lazy('budzet_list')

from django.shortcuts import get_object_or_404

class BudzetUpdateView(UpdateView):
    model = Budzet
    fields = ['naziv', 'iznos', 'datum', 'opis', 'tag']
    template_name = 'main/budzet_form.html'
    success_url = reverse_lazy('budzet_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Budzet, naziv=self.kwargs['naziv'])

class BudzetDeleteView(DeleteView):
    model = Budzet
    template_name = 'main/budzet_confirm_delete.html'
    success_url = reverse_lazy('budzet_list') 

    def get_object(self, queryset=None):
        return get_object_or_404(Budzet, naziv=self.kwargs['naziv'])

class PrihodCreateView(CreateView):
    model = Prihod
    fields = ['naziv', 'iznos', 'datum', 'opis', 'budzet']
    template_name = 'main/prihod_form.html'
    success_url = reverse_lazy('prihod_list')

class PrihodUpdateView(UpdateView):
    model = Prihod
    fields = ['naziv', 'iznos', 'datum', 'opis', 'budzet']
    template_name = 'main/prihod_form.html'
    success_url = reverse_lazy('prihod_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Prihod, naziv=self.kwargs['naziv'])

class PrihodDeleteView(DeleteView):
    model = Prihod
    template_name = 'main/prihod_confirm_delete.html'
    success_url = reverse_lazy('prihod_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Prihod, naziv=self.kwargs['naziv'])

class RashodCreateView(CreateView):
    model = Rashod
    fields = ['naziv', 'iznos', 'datum', 'opis', 'budzet']
    template_name = 'main/rashod_form.html'
    success_url = reverse_lazy('rashod_list') 

class RashodUpdateView(UpdateView):
    model = Rashod
    fields = ['naziv', 'iznos', 'datum', 'opis', 'budzet']
    template_name = 'main/rashod_form.html'
    success_url = reverse_lazy('rashod_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Rashod, naziv=self.kwargs['naziv'])

class RashodDeleteView(DeleteView):
    model = Rashod
    template_name = 'main/rashod_confirm_delete.html'
    success_url = reverse_lazy('rashod_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Rashod, naziv=self.kwargs['naziv'])

class TagCreateView(CreateView):
    model = Tag
    fields = ['naziv', 'opis', 'budzeti', 'prihodi', 'rashodi']
    template_name = 'main/kategorija_form.html'
    success_url = reverse_lazy('tag_list') 

from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

class TagUpdateView(UpdateView):
    model = Tag
    fields = ['naziv', 'opis', 'budzeti', 'prihodi', 'rashodi']
    template_name = 'main/kategorija_form.html'  
    success_url = reverse_lazy('tag_list') 

    def get_object(self, queryset=None):
        return get_object_or_404(Tag, naziv=self.kwargs['naziv'])
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'main/kategorija_confirm_delete.html'
    success_url = reverse_lazy('tag_list') 
    context_object_name = "kategorija" 
    
    def get_object(self, queryset=None):
        return get_object_or_404(Tag, naziv=self.kwargs['naziv'])
    
from rest_framework import generics, permissions
from .models import Budzet
from .serializers import BudzetSerializer

class BudzetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Budzet.objects.all()
    serializer_class = BudzetSerializer
    permission_classes = [permissions.IsAuthenticated]

class BudzetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budzet.objects.all()
    serializer_class = BudzetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Budzet, naziv=self.kwargs['naziv'])

from django.http import JsonResponse

def budget_data(request):
    budzeti = Budzet.objects.all()
    labels = [budzet.naziv for budzet in budzeti]
    values = [budzet.iznos for budzet in budzeti]

    return JsonResponse({'labels': labels, 'values': values})

from django.db.models import Sum
from django.http import JsonResponse

def income_expense_data(request):
    total_income = Prihod.objects.aggregate(Sum('iznos'))['iznos__sum'] or 0
    total_expense = Rashod.objects.aggregate(Sum('iznos'))['iznos__sum'] or 0

    return JsonResponse({
        'labels': ['Prihodi', 'Rashodi'],
        'values': [total_income, total_expense]
    })
from django.utils.timezone import now
from django.db.models.functions import TruncMonth
import datetime

def financial_trend_data(request):
    # Grupiranje prihoda i rashoda po mjesecima
    income_data = Prihod.objects.annotate(month=TruncMonth('datum')).values('month').annotate(total=Sum('iznos'))
    expense_data = Rashod.objects.annotate(month=TruncMonth('datum')).values('month').annotate(total=Sum('iznos'))

    # Kreiranje skupa svih dostupnih mjeseci
    all_months = set(entry['month'] for entry in income_data) | set(entry['month'] for entry in expense_data)

    # Sortiranje mjeseci kronološki
    sorted_months = sorted(all_months)

    labels = [month.strftime('%Y-%m') for month in sorted_months]
    income_values = []
    expense_values = []

    # Popunjavanje podataka za prihode i rashode
    for month in sorted_months:
        income_values.append(next((entry['total'] for entry in income_data if entry['month'] == month), 0))
        expense_values.append(next((entry['total'] for entry in expense_data if entry['month'] == month), 0))

    return JsonResponse({
        'labels': labels,
        'income_values': income_values,
        'expense_values': expense_values
    })

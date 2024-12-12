from django.shortcuts import render, redirect
from .models import Budzet, Prihod, Rashod, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
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

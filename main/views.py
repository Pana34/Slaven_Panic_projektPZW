from django.shortcuts import render
from .models import Budzet, Prihod, Rashod, Tag

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

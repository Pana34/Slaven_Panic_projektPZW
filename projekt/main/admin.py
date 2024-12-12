from django.contrib import admin
from main.models import *
# Register your models here.

model_list = [Budzet, Prihod, Rashod, Tag]
admin.site.register(model_list)
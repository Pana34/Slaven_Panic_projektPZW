from rest_framework import serializers
from .models import Budzet

class BudzetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budzet
        fields = ['id', 'naziv', 'iznos', 'datum', 'opis', 'tag']

from django.db import models

class Budzet(models.Model):
    naziv = models.CharField(max_length=30)
    iznos = models.FloatField()
    datum = models.DateField()
    opis = models.TextField()
    tag = models.OneToOneField('Tag', on_delete=models.SET_NULL, null=True, blank=True, related_name='budzet')
    
    def __str__(self):
        return self.naziv

class Prihod(models.Model):
    naziv = models.CharField(max_length=30)
    iznos = models.FloatField()
    datum = models.DateField()
    opis = models.TextField() 
    budzet = models.ForeignKey(Budzet, on_delete=models.CASCADE, related_name='prihodi', null=True, blank=True)
    
    def __str__(self):
        return self.naziv

class Rashod(models.Model):
    naziv = models.CharField(max_length=30)
    iznos = models.FloatField()
    datum = models.DateField()
    opis = models.TextField()
    budzet = models.ForeignKey(Budzet, on_delete=models.CASCADE, related_name='rashodi', null=True, blank=True)
    
    def __str__(self):
        return self.naziv

class Tag(models.Model):
    naziv = models.CharField(max_length=50)
    budzeti = models.ManyToManyField(Budzet, blank=True, related_name='tagovi')
    prihodi = models.ManyToManyField(Prihod, blank=True, related_name='tagovi')
    rashodi = models.ManyToManyField(Rashod, blank=True, related_name='tagovi')
    opis = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.naziv
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Budzet, Prihod, Rashod, Tag
from django.urls import reverse

class ModelTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(naziv='Štednja')
        self.budzet = Budzet.objects.create(naziv='Mjesečni Budžet', iznos=1000, datum='2024-03-02', opis='Mjesečni budžet', tag=self.tag)
        self.prihod = Prihod.objects.create(naziv='Plaća', iznos=500, datum='2024-03-01', opis='Mjesečna plaća', budzet=self.budzet)
        self.rashod = Rashod.objects.create(naziv='Stanarina', iznos=300, datum='2024-03-02', opis='Najam stana', budzet=self.budzet)

    def test_models(self):
        self.assertEqual(self.budzet.naziv, 'Mjesečni Budžet')
        self.assertEqual(self.prihod.iznos, 500)
        self.assertEqual(self.rashod.opis, 'Najam stana')

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.tag = Tag.objects.create(naziv='Putovanja')
        self.budzet = Budzet.objects.create(naziv='Godišnji Odmor', iznos=2000, datum='2024-06-01', opis='Budžet za odmor', tag=self.tag)

    def test_budzet_list_view(self):
        response = self.client.get(reverse('budzet_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Godišnji Odmor')

    def test_budzet_detail_view(self):
        response = self.client.get(reverse('budzet_detail', kwargs={'naziv': self.budzet.naziv}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Budžet za odmor')

class AuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login(self):
        login = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login)

    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  

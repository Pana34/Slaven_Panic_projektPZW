# Generated by Django 5.1.2 on 2025-03-02 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_prihod_budzet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budzet',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='budzet_set', to='main.tag'),
        ),
    ]

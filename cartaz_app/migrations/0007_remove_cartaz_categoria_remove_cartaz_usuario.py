# Generated by Django 4.2.3 on 2023-07-22 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartaz_app', '0006_cartaz_horario2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartaz',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='cartaz',
            name='usuario',
        ),
    ]

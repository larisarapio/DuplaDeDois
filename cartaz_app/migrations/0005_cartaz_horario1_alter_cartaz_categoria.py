# Generated by Django 4.2.3 on 2023-07-22 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartaz_app', '0004_cartaz_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartaz',
            name='horario1',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='cartaz',
            name='categoria',
            field=models.CharField(choices=[('ADMINISTRADOR', 'administrador'), ('USUARIO', 'usuario')], default='administrador', max_length=100, null=True),
        ),
    ]

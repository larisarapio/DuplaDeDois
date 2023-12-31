# Generated by Django 4.2.3 on 2023-07-22 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagemUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('PESSOA', 'pessoa'), ('PESSOADEFICIENTE', 'pessoaDeficiente')], default='administrador', max_length=100, null=True)),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, upload_to='imagem/%Y/%m%d')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

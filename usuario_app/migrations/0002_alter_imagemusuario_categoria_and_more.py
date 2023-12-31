# Generated by Django 4.2.3 on 2023-07-24 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemusuario',
            name='categoria',
            field=models.CharField(choices=[('PESSOA', 'pessoa'), ('PESSOADEFICIENTE', 'pessoaDeficiente')], default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='imagemusuario',
            name='foto',
            field=models.ImageField(blank=True, upload_to='imagem/%Y/%m/%d/'),
        ),
    ]

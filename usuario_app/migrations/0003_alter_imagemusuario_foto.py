# Generated by Django 4.2.3 on 2023-07-25 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario_app', '0002_alter_imagemusuario_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemusuario',
            name='foto',
            field=models.ImageField(upload_to='imagem/%Y/%m/%d/'),
        ),
    ]

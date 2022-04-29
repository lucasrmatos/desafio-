# Generated by Django 4.0.4 on 2022-04-19 23:34

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0002_remove_candidato_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='telefone',
            field=phone_field.models.PhoneField(blank=True, help_text='celular', max_length=31),
        ),
    ]

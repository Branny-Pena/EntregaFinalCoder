# Generated by Django 4.0.5 on 2022-07-20 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoFinalApp', '0004_delete_persona'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='user',
            new_name='usuario',
        ),
    ]

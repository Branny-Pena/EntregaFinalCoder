# Generated by Django 4.0.5 on 2022-07-25 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProyectoFinalApp', '0011_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='autor', to=settings.AUTH_USER_MODEL),
        ),
    ]

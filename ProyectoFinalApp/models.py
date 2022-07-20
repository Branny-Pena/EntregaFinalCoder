from django.db import models
from django.contrib.auth.models import User

class perfil(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media\profilePics', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    ROLES = (
            ('admin', 'Administrador'),
            ('user', 'Usuario'))
    
    rol = models.CharField(max_length=10, choices=ROLES, default='user')
    
    

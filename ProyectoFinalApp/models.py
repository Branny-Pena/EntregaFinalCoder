from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media\profilePics', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
            return self.usuario.username
    
class Mensaje(models.Model):
        origen = models.ForeignKey(User, on_delete=models.CASCADE, related_name='origen')
        destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinatario')
        mensaje = models.TextField(max_length=1000, blank=True, null=True)
        actualizado = models.DateTimeField(auto_now=True)
        creado = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
                return self.mensaje

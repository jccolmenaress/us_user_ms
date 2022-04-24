import email
import profile
from django.db import models
import uuid

class Profile(models.Model):
    id = models.CharField(max_length=250, primary_key=True)
    email = models.EmailField(max_length=100,unique=True)
    name = models.CharField(max_length = 200)
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=300, blank=True)#esto va en el otro micro servicio y es un archivo markdown

    def __str__(self):
        return self.name
    
    def listAtributes(self):
        return vars(self)
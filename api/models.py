from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    endereco = models.CharField(max_length=128)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nome
    
    def get_nome(self):
        return self.nome
    
    def get_email(self):
        return self.email
    
    def get_endereco(self):
        return self.endereco

from django.db import models
from django.core.validators import EmailValidator


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.Charfield(max_length=50, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=True,
                              validators=[EmailValidator(message="Correo invalido")])
    role = models.Charfield(max_length=20, choices=[
        ('admin', 'Admin'),
        ('films', 'Films'),
        ('people', 'People'),
        ('locations', 'Locations'),
        ('species', 'Species'),
        ('vehicles', 'Vehicles')
    ])

    def __str__(self):
        return self.username

from django.db import models

class Auto(models.Model):
    TIPO_CHOICES = [
        ('auto', 'Autos'),
        ('pickup-comercial', 'Pickups y Comerciales'),
        ('suv-crossover', 'SUVs y Crossovers'),
    ]

    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    foto = models.ImageField(upload_to='autosapp/images')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.modelo

class Meta:
    app_label = 'autosapp'


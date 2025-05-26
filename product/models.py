from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='nombre de la categoria')
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name='nombre del producto')
    description = models.CharField(max_length=150, verbose_name='description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='precios')
    imagen = models.ImageField(
        upload_to='products/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png', 'webp'],  # Extensiones permitidas
                message='Solo se permiten imágenes JPG, PNG o WEBP'
            )
        ],
        blank=True,
        null=True
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='categoria')
    available = models.BooleanField(default=True, verbose_name='Disponibilidad')
    
    def __str__(self):
        return self.name
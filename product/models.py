from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='nombre de la categoria')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías' 
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name='nombre del producto')
    description = models.CharField(max_length=150, verbose_name='descripcion del producto')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='precio')
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
    
    class Meta:
        verbose_name = 'Producto' 
        verbose_name_plural = 'Productos' 
    
    def __str__(self):
        return self.name
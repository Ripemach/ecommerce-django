from distutils.command.upload import upload
from enum import unique
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 20, unique = True)
    description = models.CharField(max_length = 255, blank = True)
    ## slug es un campo utilizado en eCommerce que representa a la entidad
    slug = models.CharField(max_length = 100, unique = True)
    cat_image = models.ImageField(upload_to = 'photos/categories', blank = True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
        # 'products_by_category' fue definida en store/urls.py 
        # el sefl.slug lo que hace es agregarle al path el slug de la categoria
        # http://localhost:8000/store/computadora

    # Esta data debera ser visible dentro del dashboard de Django asi que:
    def __str__(self):
        return self.category_name


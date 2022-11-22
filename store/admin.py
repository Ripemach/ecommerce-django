from django.contrib import admin
from .models import Product

# Register your models here.
#Creamos una clase que permita agregar ciertas propiedades de listar a los productos dentro del grid de
#administración del django
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    # Como queremos llenar el slug
    prepopulated_fields = {'slug': ('product_name',)}

#Una vez tenemos la clase lista, registramos la entidad Product
admin.site.register(Product,ProductAdmin)
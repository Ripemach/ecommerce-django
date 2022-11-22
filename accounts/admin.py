from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    # Cuando se le de click a una columna este link vaya al detalle del usuario
    list_display_link = ('email','first_name','last_name')
    # queremos que los campos de lectura sean:
    readonly_fields = ('last_login','date_joined')
    #queremos que se organice de forma ascendente dependiendo de la fecha en la cual 
    #el usuario se unio a la aplicación
    ordering = ('-date_joined',) ## Ojo conponer la coma al final

    # Inicializamos el filtro horizontal y los siguientes parametros
    filter_horizontal= ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
# Y le pasamos como parametro tambien el AccountAdmin que creamos posteriormente
admin.site.register(Account,AccountAdmin)

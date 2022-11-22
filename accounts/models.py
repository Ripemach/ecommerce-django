from distutils.command.build_scripts import first_line_re
import email
from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
# Clase que tienelas operaciones que permiten crear un nuevo usuario y tambien un 
# usuario superadmin. Esta clase se crea despues de haber cxeado la clase Account
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener un eMail')

        if not username:
            raise ValueError('El usuario debe tener un username')

        # Definición de un objeto de tipo user
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # Función que permite crear un superusuario
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=50)

    # Campos atributos de django obligatorios
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

   
    # Ahora lo que queremos es que cuando el usuario acceda lo haga mediante su correo y no con el usarname
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    # Incluimos una instancia de MyAccountManager en el modelo accounts para incluir los metodos
    # create_user y create_superuser dentro del modelo principal Account
    # El MyAccountManager fue creado posteriormente a Account
    objects = MyAccountManager()
    # de esta forma ya podremos usar create_user y create_superuser instanciando Account

    def __str__(self):
        return self.email

    # Averiguar si tiene permisos
    # Función para acceder a labores de administración
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Y si es administrador tambien hay que verificar si tiene acceso a los módulos
    def has_module_perms(self, add_label):
        return True

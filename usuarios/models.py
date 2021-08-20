from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    pass
    # add additional fields in here

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return self.username
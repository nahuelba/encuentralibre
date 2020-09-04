from django.db import models
from usuario.models import Usuario

# Create your models here.
class Busqueda(models.Model):
    busqueda=models.CharField(max_length=30)
    precio_min=models.IntegerField(verbose_name="Precio mínimo")
    precio_max=models.IntegerField(verbose_name="Precio máximo")
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.busqueda





class Resultado(models.Model):
    busqueda=models.ForeignKey(Busqueda, on_delete=models.CASCADE)
    ids=models.CharField(max_length=30)
    titulo=models.CharField(max_length=80)
    precio=models.IntegerField()
    link=models.URLField(max_length=200)
    fecha=models.DateTimeField(auto_now_add=True)
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-fecha']

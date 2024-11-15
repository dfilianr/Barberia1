from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from core.models import Barberia, Barbero
from Barberia.funciones import Opciones
from django.utils import timezone
from datetime import timedelta, datetime
from django.utils.timezone import now

opciones = Opciones()
PLANES = opciones.planes()  # Llamada al método de instancia
horarioAtencion = opciones.horario_atencion()

class Agenda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=False, null=True,default=timezone.now().date())
    plan = models.CharField(max_length=1, choices=PLANES, default=PLANES[0][0], blank=True, null=True)
    barbero = models.ForeignKey(Barbero,on_delete=models.CASCADE, default=id(1))
    horarioAtencion = models.CharField(max_length=1, choices=horarioAtencion, default=horarioAtencion[0][0], blank=True, null=True)

    def clean(self):
        # Verificar si ya existe una agenda para el mismo barbero, día y hora
        if Agenda.objects.exclude(id=self.id).filter(
                fecha__date=self.fecha.date(),
                horarioAtencion=self.horarioAtencion,
                barbero=self.barbero
        ).exists():
            raise ValidationError("El barbero ya tiene una agenda para esta hora en este día.")
        # if Agenda.objects.filter(fecha__date=self.fecha.date(), horarioAtencion=self.horarioAtencion).exists():
        #     raise ValidationError("Ya existe una agenda para esta hora en este día.")
        #
        # if Agenda.objects.filter(fecha__date=self.fecha.date(), horarioAtencion=self.horarioAtencion).exists():
        #     raise ValidationError("Ya existe una agenda para esta hora en este día.")


    def __str__(self):
        return str(self.barbero)
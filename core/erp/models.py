from django.db import models
from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
from core.user.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from core.user.models import Empresa,Unidad,Puesto
from simple_history.models import HistoricalRecords
# Create your models here.
class Trabajadores(models.Model):
    tipo = models.CharField(max_length=3,choices=[('1',"DNI"),('2',"C.E"),('3',"PASAPORTE")],blank=True,null=True)
    documento = models.CharField(max_length=10,verbose_name="Documento")
    nombre = models.CharField(max_length=25,verbose_name="Nombres")
    apellidos = models.CharField(max_length=50,verbose_name="Apellidos")
    telefono = models.PositiveIntegerField(verbose_name="Celular",null=True,blank=True)
    direccion = models.CharField(max_length=100,verbose_name="Direccion",null=True,blank=True)
    sctr = models.FileField(upload_to='sctr/',verbose_name="SCTR",blank=True,null=True)
    history = HistoricalRecords()

    def toJSON(self):
        item = model_to_dict(self)
        item['sctr'] = self.get_file()
        return item
    class Meta:
        verbose_name = "Trabajadores"
        verbose_name_plural = "Trabajadores"
        db_table = "trabajadores"
        ordering = ['id']
    def get_file(self):
        if self.sctr:
            return '{}{}'.format(MEDIA_URL, self.sctr)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellidos}"
class Vehiculos(models.Model):
    trabajador = models.ForeignKey(Trabajadores,on_delete=models.CASCADE,verbose_name="Trabajador",blank=True,null=True)
    marca = models.CharField(max_length=15,verbose_name='Marca del Vehiculo',default='')
    modelo = models.CharField(max_length=20,verbose_name="Modelo vel Vehiculo",default='')
    placa = models.CharField(max_length=6,verbose_name="Placa de rodaje",default='')
    fv_soat = models.DateField(auto_now=True,verbose_name="SOAT-Fecha de Vencimiento")
    history = HistoricalRecords()

    def toJSON(self):
        item = model_to_dict(self)
        item['trabajador'] = self.trabajador.id
        return item
    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"
        db_table = "vehiculos"
        ordering = ['id']
class AsignacionEPPS(models.Model):
    trabajador = models.ForeignKey(Trabajadores,on_delete=models.CASCADE,verbose_name="Trabajador",blank=True,null=True)
    casco = models.BooleanField(default=False,verbose_name="Casco")
    barbiquejo = models.BooleanField(default=False,verbose_name="Barbiquejo")
    botas = models.BooleanField(default=False,verbose_name="Botas punta de acero")
    tapones = models.BooleanField(default=False,verbose_name="Tapones de oido")
    lentes = models.BooleanField(default=False,verbose_name="Lentes de seguridad")
    chaleco = models.BooleanField(default=False,verbose_name="Chaleco reflectivo")
    respirador = models.BooleanField(default=False,verbose_name="Respirador doble via")
    history = HistoricalRecords()

    def toJSON(self):
        item = model_to_dict(self)
        item['trabajador'] = self.trabajador.id
        return item
    class Meta:
        verbose_name = "AsignacionEPPS"
        verbose_name_plural = "AsignacionEPPS"
        db_table = 'asignacion_epps'
        ordering = ['id']
class AsignacionEV(models.Model):#ASIGNACION DE EQUIPO VEHICULAR
    trabajador = models.ForeignKey(Trabajadores,on_delete=models.CASCADE,verbose_name="Trabajador",blank=True,null=True)
    botiquin = models.BooleanField(default=False,verbose_name="Botiquin")
    extintor = models.BooleanField(default=False,verbose_name="Extintor")
    triangulo_s = models.BooleanField(default=False,verbose_name="Triangulo de Seguridad")
    cono_s = models.BooleanField(default=False,verbose_name="Cono de seguridad")
    taco = models.BooleanField(default=False,verbose_name="taco")
    pertiga = models.BooleanField(default=False,verbose_name="pertiga")
    circulina = models.BooleanField(default=False,verbose_name="Circulina")
    history = HistoricalRecords()

    def toJSON(self):
        item = model_to_dict(self)
        item['trabajador'] = self.trabajador.id
        return item
    class Meta:
        verbose_name = 'AsignacionEV'
        verbose_name = 'AsignacionEVS'
        db_table = 'asignacion_ev'
        ordering = ['id']
class IngresoSalida(models.Model):
    documento = models.CharField(max_length=11,verbose_name="N° Documento",null=True,blank=True)
    nombres = models.CharField(max_length=150,verbose_name="Nombre Completo",null=True,blank=True)
    fecha = models.DateField(auto_now_add=True,verbose_name="Fecha",null=True,blank=True)
    hora = models.TimeField(auto_now_add=True,verbose_name="Hora de salida",null=True,blank=True)
    tipo = models.CharField(max_length=15,choices=[("1",'INGRESO'),("2","SALIDA")])
    motivo = models.CharField(max_length=200,verbose_name="Motivo del ingreso o salida")
    history = HistoricalRecords()
    class Meta:
        verbose_name = "IngresoSalida"
        verbose_name_plural = "IngresosSalidas"
        db_table = "ingresos_salidas"
        ordering = ['id']
    def toJSON(self):
        item = model_to_dict(self)
        return item
class Salas(models.Model):
    sala = models.CharField(max_length=100,verbose_name="Sala",unique=True)
    estado= models.IntegerField(verbose_name="Estado",default=0,null=True,blank=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.DO_NOTHING,verbose_name="Empresa",null=True,blank=True)
    capacidad = models.PositiveIntegerField(verbose_name="Capacidad",null=True,blank=True)
    unidad = models.ForeignKey(Unidad,on_delete=models.DO_NOTHING,verbose_name="unidad",null=True,blank=True)
    puesto = models.ForeignKey(Puesto,on_delete=models.DO_NOTHING,verbose_name="puesto",null=True,blank=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        db_table = 'salas'
        ordering = ['id']
    def toJSON(self):
        item = model_to_dict(self)
        return item
    def __str__(self) -> str:
        return self.sala
  
class Parqueo(models.Model):
    numero = models.CharField(max_length=5,verbose_name="Numero de Parqueo",unique=False)
    estado = models.BooleanField(default=True,verbose_name="Estado",null=True,blank=True)
    nombre = models.CharField(max_length=150,verbose_name="Nombre del parqueo",null=True,blank=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.DO_NOTHING,verbose_name="Empresa",null=True,blank=True)
    unidad = models.ForeignKey(Unidad,on_delete=models.DO_NOTHING,verbose_name="unidad",null=True,blank=True)
    puesto = models.ForeignKey(Puesto,on_delete=models.DO_NOTHING,verbose_name="puesto",null=True,blank=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Parqueo"
        verbose_name_plural = "Parqueos"
        db_table = 'parqueos'
        ordering = ['id']
    def toJSON(self):
        item = model_to_dict(self)
        return item
    def __str__(self) -> str:
        return self.numero
class Visitas(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="Usuario que Autoriza",null=True,blank=True)
    tipo_documento = models.CharField(max_length=10,choices=[("1","DNI"),("2","C.E"),("3","PASAPORTE")],verbose_name="TIPO DOCUMENTO",blank=True,null=True)
    dni = models.CharField(max_length=10,verbose_name="N° Documento")
    nombre = models.CharField(max_length=50,verbose_name="Nombres")
    apellidos = models.CharField(max_length=50,verbose_name="Apellidos")
    empresa = models.CharField(max_length=150,verbose_name="Empresa",null=True,blank=True)
    cargo = models.CharField(max_length=50,verbose_name="Cargo",null=True,blank=True)
    fecha = models.DateField(auto_now=False,verbose_name="Fecha")
    h_inicio = models.TimeField(auto_now=False,verbose_name="Hora de inicio")
    h_termino = models.TimeField(auto_now=False,verbose_name="Hora de Finalizacion",null=True,blank=True)
    h_llegada = models.TimeField(auto_now=False,verbose_name="Hora de llegada",null=True,blank=True)
    h_salida = models.TimeField(auto_now=False,verbose_name="Hora de Salida",null=True,blank=True)
    p_visita = models.ForeignKey(Trabajadores,on_delete=models.DO_NOTHING,null=True,blank=True,verbose_name="Persona a quien visita")
    motivo = models.CharField(max_length=150,verbose_name="Motivo")
    sala = models.ForeignKey(Salas,on_delete = models.DO_NOTHING,null=True,blank=True)
    v_marca = models.CharField(max_length=20,verbose_name="Marca del Vehiculo",null=True,blank=True)
    v_modelo = models.CharField(max_length=20,verbose_name="Modelo del vehiculo",null=True,blank=True)
    v_placa =  models.CharField(max_length=10,verbose_name="Placa de rodaje",null=True,blank=True)
    fv_soat = models.CharField(max_length=50,verbose_name="Fecha de vencimiento del SOAT",null=True,blank=True)
    sctr_salud = models.FileField(verbose_name="SCTR-SALUD",null=True,blank=True)
    n_parqueo = models.ForeignKey(Parqueo,on_delete=models.DO_NOTHING,verbose_name="Numero de Parqueo",null=True,blank=True)
    estado = models.CharField(max_length=10,choices=[('1','PROGRAMADO'),('2','EN CURSO'),('3','FINALIZO')],null=True,blank=True)
    guias = models.FileField(upload_to='guias/',verbose_name="Guias de remision",blank=True,null=True)
    cantidad = models.CharField(verbose_name="Cantidad",max_length=20,blank=True,null=True)
    tipo = models.CharField(max_length=3,choices=[('1','VISITA'),("2","COURRIER/DELIVERY")],default='1')
    observacion = models.CharField(max_length=100,verbose_name="Observaciones",blank=True,null=True)
    documentos = models.CharField(max_length=250,verbose_name="Documentos",null=True,blank=True)
    history = HistoricalRecords()

    def get_file(self,file):
        if file:
            return '{}{}'.format(MEDIA_URL, file)
        return '{}{}'.format(STATIC_URL, 'img/nopdf.jpg')
    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'
        db_table = 'visitas'
    def toJSON(self):
        item = model_to_dict(self)
        item['user'] = self.user.id
        item['guias'] = self.get_file(self.guias)
        item['sctr_salud'] = self.get_file(self.sctr_salud)
        item['names'] = f"{self.nombre} {self.apellidos}"
        return item
class Asistentes(models.Model):
    visita = models.ForeignKey(Visitas,on_delete=models.DO_NOTHING,verbose_name="Visita",unique=False)
    documento = models.CharField(max_length=11,verbose_name="n° documento")
    nombre = models.CharField(max_length=50,verbose_name="Nombres")
    apellidos = models.CharField(max_length=50,verbose_name="Apellidos")
    empresa = models.CharField(max_length=150,verbose_name="Empresa",null=True,blank=True)
    marca_v = models.CharField(max_length=50,verbose_name="Marca del vehiculo",null=True,blank=True)
    modelo_v = models.CharField(max_length=20,verbose_name="Modelo del vehiculo",null=True,blank=True)
    placa_v = models.CharField(max_length=8,verbose_name="Placa del vehiculo",null=True,blank=True)
    soat_v = models.DateField(default=date.today,verbose_name="FV-SOAT",null=True,blank=True)
    sctr = models.FileField(upload_to='strc/', verbose_name="STRC",null=True,blank=True)
    n_parqueo = models.ForeignKey(Parqueo,on_delete=models.DO_NOTHING,verbose_name="Parqueo",null=True,blank=True)
    history = HistoricalRecords()
    class Meta:
        verbose_name = "asinten"
        verbose_name_plural = 'asistentes'
        db_table = 'asis_visitas'
    def __str__(self) -> str:
        return str(self.visita)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['visita'] = self.visita.id
        item['sctr'] = self.get_file()
        return item

    def get_file(self):
        if self.sctr:
            return '{}{}'.format(MEDIA_URL, self.sctr)
        return '{}{}'.format(STATIC_URL, 'img/nopdf.jpg')

@receiver(post_save, sender=Trabajadores)
def add_automatic(sender, instance, created, **kwargs):
    if created:
        AsignacionEPPS.objects.create(trabajador=instance)
        Vehiculos.objects.create(trabajador=instance)
        AsignacionEV.objects.create(trabajador=instance)


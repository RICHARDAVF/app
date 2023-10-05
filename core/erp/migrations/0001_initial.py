# Generated by Django 4.2.3 on 2023-10-03 14:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionEPPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casco', models.BooleanField(default=False, verbose_name='Casco')),
                ('barbiquejo', models.BooleanField(default=False, verbose_name='Barbiquejo')),
                ('botas', models.BooleanField(default=False, verbose_name='Botas punta de acero')),
                ('tapones', models.BooleanField(default=False, verbose_name='Tapones de oido')),
                ('lentes', models.BooleanField(default=False, verbose_name='Lentes de seguridad')),
                ('chaleco', models.BooleanField(default=False, verbose_name='Chaleco reflectivo')),
                ('respirador', models.BooleanField(default=False, verbose_name='Respirador doble via')),
            ],
            options={
                'verbose_name': 'AsingacionEPPS',
                'verbose_name_plural': 'AsignacionEPPS',
                'db_table': 'asignacion_epps',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AsignacionEV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('botiquin', models.BooleanField(default=False, verbose_name='Botiquin')),
                ('extintor', models.BooleanField(default=False, verbose_name='Extintor')),
                ('triangulo_s', models.BooleanField(default=False, verbose_name='Triangulo de Seguridad')),
                ('cono_s', models.BooleanField(default=False, verbose_name='Cono de seguridad')),
                ('taco', models.BooleanField(default=False, verbose_name='taco')),
                ('pertiga', models.BooleanField(default=False, verbose_name='pertiga')),
                ('circulina', models.BooleanField(default=False, verbose_name='Circulina')),
            ],
            options={
                'verbose_name': 'AsignacionEVS',
                'db_table': 'asignacion_ev',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Asistentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=11, verbose_name='n° documento')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('empresa', models.CharField(blank=True, max_length=150, null=True, verbose_name='Empresa')),
                ('marca_v', models.CharField(max_length=50, verbose_name='Marca del vehiculo')),
                ('modelo_v', models.CharField(max_length=20, verbose_name='Modelo del vehiculo')),
                ('placa_v', models.CharField(max_length=8, verbose_name='Placa del vehiculo')),
                ('soat_v', models.DateField(default=datetime.date.today, verbose_name='FV-SOAT')),
                ('strc', models.FileField(upload_to='strc/', verbose_name='STRC')),
            ],
            options={
                'verbose_name': 'asinten',
                'verbose_name_plural': 'asistentes',
                'db_table': 'asis_visitas',
            },
        ),
        migrations.CreateModel(
            name='IngresoSalida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(blank=True, max_length=11, null=True, verbose_name='N° Documento')),
                ('nombres', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre Completo')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('h_salida', models.TimeField(blank=True, null=True, verbose_name='Hora de salida')),
                ('h_entrada', models.TimeField(blank=True, null=True, verbose_name='Hora de ingreso')),
            ],
            options={
                'verbose_name': 'IngresoSalida',
                'verbose_name_plural': 'IngresosSalidas',
                'db_table': 'ingresos_salidas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Parqueo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=5, unique=True, verbose_name='Numero de Parqueo')),
                ('estado', models.BooleanField(blank=True, default=True, null=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Parqueo',
                'verbose_name_plural': 'Parqueos',
                'db_table': 'parqueos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.CharField(max_length=10, unique=True, verbose_name='Sala')),
                ('estado', models.IntegerField(blank=True, default=0, null=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
                'db_table': 'salas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Trabajadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, choices=[('1', 'DNI'), ('2', 'C.E'), ('3', 'PASAPORTE')], max_length=3, null=True)),
                ('documento', models.CharField(max_length=10, verbose_name='Documento')),
                ('nombre', models.CharField(max_length=25, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('sctr', models.FileField(blank=True, null=True, upload_to='sctr/', verbose_name='SCTR')),
            ],
            options={
                'verbose_name': 'Trabajadores',
                'verbose_name_plural': 'Trabajadores',
                'db_table': 'trabajadores',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(default='', max_length=15, verbose_name='Marca del Vehiculo')),
                ('modelo', models.CharField(default='', max_length=20, verbose_name='Modelo vel Vehiculo')),
                ('placa', models.CharField(default='', max_length=6, verbose_name='Placa de rodaje')),
                ('fv_soat', models.DateField(auto_now=True, verbose_name='SOAT-Fecha de Vencimiento')),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
                'db_table': 'vehiculos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Visitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(blank=True, choices=[('1', 'DNI'), ('2', 'C.E'), ('3', 'PASAPORTE')], max_length=10, null=True, verbose_name='TIPO DOCUMENTO')),
                ('dni', models.CharField(max_length=10, verbose_name='N° Documento')),
                ('nombre', models.CharField(max_length=15, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('empresa', models.CharField(blank=True, max_length=150, null=True, verbose_name='Empresa')),
                ('cargo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cargo')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('h_inicio', models.TimeField(verbose_name='Hora de inicio')),
                ('h_termino', models.TimeField(blank=True, null=True, verbose_name='Hora de termino')),
                ('p_visita', models.CharField(blank=True, max_length=150, null=True, verbose_name='Persona a quien visita')),
                ('motivo', models.CharField(max_length=150, verbose_name='Motivo')),
                ('v_marca', models.CharField(blank=True, max_length=20, null=True, verbose_name='Marca del Vehiculo')),
                ('v_modelo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo del vehiculo')),
                ('v_placa', models.CharField(blank=True, max_length=10, null=True, verbose_name='Placa de rodaje')),
                ('fv_soat', models.CharField(blank=True, max_length=50, null=True, verbose_name='SOAT-VEHICULO')),
                ('sctr_salud', models.CharField(blank=True, max_length=30, null=True, verbose_name='SCTR-SALUD')),
                ('estado', models.CharField(blank=True, choices=[('1', 'PROGRAMÓ'), ('2', 'ENTRÓ'), ('3', 'VISITÓ')], max_length=10, null=True)),
                ('guias', models.FileField(blank=True, null=True, upload_to='guias/', verbose_name='Guias de remision')),
                ('cantidad', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cantidad')),
                ('tipo', models.CharField(choices=[('1', 'VISITA'), ('2', 'COURRIER'), ('3', 'DELIVERY')], default='1', max_length=3)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Observaciones')),
                ('n_parqueo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp.parqueo', verbose_name='Numero de Parqueo')),
                ('sala', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp.salas')),
            ],
            options={
                'verbose_name': 'Visita',
                'verbose_name_plural': 'Visitas',
                'db_table': 'visitas',
            },
        ),
    ]

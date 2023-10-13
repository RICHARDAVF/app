# Generated by Django 4.2.3 on 2023-10-13 14:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_historicaluser_historicalunidad_historicalempresa'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0011_parqueo_nombre_alter_visitas_fv_soat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalVisitas',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('tipo_documento', models.CharField(blank=True, choices=[('1', 'DNI'), ('2', 'C.E'), ('3', 'PASAPORTE')], max_length=10, null=True, verbose_name='TIPO DOCUMENTO')),
                ('dni', models.CharField(max_length=10, verbose_name='N° Documento')),
                ('nombre', models.CharField(max_length=15, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('empresa', models.CharField(blank=True, max_length=150, null=True, verbose_name='Empresa')),
                ('cargo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cargo')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('h_inicio', models.TimeField(verbose_name='Hora de inicio')),
                ('h_termino', models.TimeField(blank=True, null=True, verbose_name='Hora de Finalizacion')),
                ('h_llegada', models.TimeField(blank=True, null=True, verbose_name='Hora de llegada')),
                ('h_salida', models.TimeField(blank=True, null=True, verbose_name='Hora de Salida')),
                ('motivo', models.CharField(max_length=150, verbose_name='Motivo')),
                ('v_marca', models.CharField(blank=True, max_length=20, null=True, verbose_name='Marca del Vehiculo')),
                ('v_modelo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo del vehiculo')),
                ('v_placa', models.CharField(blank=True, max_length=10, null=True, verbose_name='Placa de rodaje')),
                ('fv_soat', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fecha de vencimiento del SOAT')),
                ('sctr_salud', models.CharField(blank=True, max_length=30, null=True, verbose_name='SCTR-SALUD')),
                ('estado', models.CharField(blank=True, choices=[('1', 'PROGRAMADO'), ('2', 'EN CURSO'), ('3', 'FINALIZO')], max_length=10, null=True)),
                ('guias', models.TextField(blank=True, max_length=100, null=True, verbose_name='Guias de remision')),
                ('cantidad', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cantidad')),
                ('tipo', models.CharField(choices=[('1', 'VISITA'), ('2', 'COURRIER/DELIVERY')], default='1', max_length=3)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Observaciones')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('n_parqueo', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='erp.parqueo', verbose_name='Numero de Parqueo')),
                ('p_visita', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='erp.trabajadores', verbose_name='Persona a quien visita')),
                ('sala', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='erp.salas')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que Autoriza')),
            ],
            options={
                'verbose_name': 'historical Visita',
                'verbose_name_plural': 'historical Visitas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalVehiculos',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('marca', models.CharField(default='', max_length=15, verbose_name='Marca del Vehiculo')),
                ('modelo', models.CharField(default='', max_length=20, verbose_name='Modelo vel Vehiculo')),
                ('placa', models.CharField(default='', max_length=6, verbose_name='Placa de rodaje')),
                ('fv_soat', models.DateField(blank=True, editable=False, verbose_name='SOAT-Fecha de Vencimiento')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('trabajador', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='erp.trabajadores', verbose_name='Trabajador')),
            ],
            options={
                'verbose_name': 'historical Vehiculo',
                'verbose_name_plural': 'historical Vehiculos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTrabajadores',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, choices=[('1', 'DNI'), ('2', 'C.E'), ('3', 'PASAPORTE')], max_length=3, null=True)),
                ('documento', models.CharField(max_length=10, verbose_name='Documento')),
                ('nombre', models.CharField(max_length=25, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('telefono', models.PositiveIntegerField(blank=True, null=True, verbose_name='Celular')),
                ('direccion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Direccion')),
                ('sctr', models.TextField(blank=True, max_length=100, null=True, verbose_name='SCTR')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Trabajadores',
                'verbose_name_plural': 'historical Trabajadores',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSalas',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('sala', models.CharField(db_index=True, max_length=100, verbose_name='Sala')),
                ('estado', models.IntegerField(blank=True, default=0, null=True, verbose_name='Estado')),
                ('capacidad', models.PositiveIntegerField(blank=True, null=True, verbose_name='Capacidad')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('empresa', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.empresa', verbose_name='Empresa')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('puesto', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.puesto', verbose_name='puesto')),
                ('unidad', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.unidad', verbose_name='unidad')),
            ],
            options={
                'verbose_name': 'historical Sala',
                'verbose_name_plural': 'historical Salas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalParqueo',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('numero', models.CharField(max_length=5, verbose_name='Numero de Parqueo')),
                ('estado', models.BooleanField(blank=True, default=True, null=True, verbose_name='Estado')),
                ('nombre', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre del parqueo')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('empresa', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.empresa', verbose_name='Empresa')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('puesto', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.puesto', verbose_name='puesto')),
                ('unidad', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.unidad', verbose_name='unidad')),
            ],
            options={
                'verbose_name': 'historical Parqueo',
                'verbose_name_plural': 'historical Parqueos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIngresoSalida',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('documento', models.CharField(blank=True, max_length=11, null=True, verbose_name='N° Documento')),
                ('nombres', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre Completo')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('h_salida', models.TimeField(blank=True, null=True, verbose_name='Hora de salida')),
                ('h_entrada', models.TimeField(blank=True, null=True, verbose_name='Hora de ingreso')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical IngresoSalida',
                'verbose_name_plural': 'historical IngresosSalidas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAsistentes',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('documento', models.CharField(max_length=11, verbose_name='n° documento')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('empresa', models.CharField(blank=True, max_length=150, null=True, verbose_name='Empresa')),
                ('marca_v', models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca del vehiculo')),
                ('modelo_v', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo del vehiculo')),
                ('placa_v', models.CharField(blank=True, max_length=8, null=True, verbose_name='Placa del vehiculo')),
                ('soat_v', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='FV-SOAT')),
                ('sctr', models.TextField(blank=True, max_length=100, null=True, verbose_name='STRC')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('n_parqueo', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='erp.parqueo', verbose_name='Parqueo')),
                ('visita', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='erp.visitas', verbose_name='Visita')),
            ],
            options={
                'verbose_name': 'historical asinten',
                'verbose_name_plural': 'historical asistentes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAsignacionEV',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('botiquin', models.BooleanField(default=False, verbose_name='Botiquin')),
                ('extintor', models.BooleanField(default=False, verbose_name='Extintor')),
                ('triangulo_s', models.BooleanField(default=False, verbose_name='Triangulo de Seguridad')),
                ('cono_s', models.BooleanField(default=False, verbose_name='Cono de seguridad')),
                ('taco', models.BooleanField(default=False, verbose_name='taco')),
                ('pertiga', models.BooleanField(default=False, verbose_name='pertiga')),
                ('circulina', models.BooleanField(default=False, verbose_name='Circulina')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('trabajador', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='erp.trabajadores', verbose_name='Trabajador')),
            ],
            options={
                'verbose_name': 'historical AsignacionEVS',
                'verbose_name_plural': 'historical AsignacionEVSs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAsignacionEPPS',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('casco', models.BooleanField(default=False, verbose_name='Casco')),
                ('barbiquejo', models.BooleanField(default=False, verbose_name='Barbiquejo')),
                ('botas', models.BooleanField(default=False, verbose_name='Botas punta de acero')),
                ('tapones', models.BooleanField(default=False, verbose_name='Tapones de oido')),
                ('lentes', models.BooleanField(default=False, verbose_name='Lentes de seguridad')),
                ('chaleco', models.BooleanField(default=False, verbose_name='Chaleco reflectivo')),
                ('respirador', models.BooleanField(default=False, verbose_name='Respirador doble via')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('trabajador', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='erp.trabajadores', verbose_name='Trabajador')),
            ],
            options={
                'verbose_name': 'historical AsingacionEPPS',
                'verbose_name_plural': 'historical AsignacionEPPS',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]

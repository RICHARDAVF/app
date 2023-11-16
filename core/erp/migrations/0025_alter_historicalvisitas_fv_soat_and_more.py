# Generated by Django 4.2.3 on 2023-11-16 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0024_alter_cargotrabajador_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalvisitas',
            name='fv_soat',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento del SOAT'),
        ),
        migrations.AlterField(
            model_name='visitas',
            name='fv_soat',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento del SOAT'),
        ),
        migrations.CreateModel(
            name='EquiposProteccionVisitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('botiquin', models.BooleanField(default=False, verbose_name='Botiquin')),
                ('extintor', models.BooleanField(default=False, verbose_name='Extintor')),
                ('triangulo', models.BooleanField(default=False, verbose_name='Triangulo de Seguridad')),
                ('cono_s', models.BooleanField(default=False, verbose_name='Cono de seguridad')),
                ('taco', models.BooleanField(default=False, verbose_name='Taco')),
                ('pertiga', models.BooleanField(default=False, verbose_name='Pertiga')),
                ('circulina', models.BooleanField(default=False, verbose_name='Circulina')),
                ('casco', models.BooleanField(default=False, verbose_name='Casco')),
                ('barbiquejo', models.BooleanField(default=False, verbose_name='Barbiquejo')),
                ('botas', models.BooleanField(default=False, verbose_name='Botas punta de acero')),
                ('tapones', models.BooleanField(default=False, verbose_name='Tapones de oido')),
                ('lentes', models.BooleanField(default=False, verbose_name='Lentes de seguridad')),
                ('chaleco', models.BooleanField(default=False, verbose_name='Chaleco reflectivo')),
                ('respirador', models.BooleanField(default=False, verbose_name='Respirador doble via')),
                ('visitante', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to='erp.visitas', verbose_name='Visitante')),
            ],
            options={
                'verbose_name': 'Equipo de Proteccion del visitante',
                'verbose_name_plural': 'Equipos de seguridad de los visitantes',
                'db_table': 'ep_visitante',
            },
        ),
    ]
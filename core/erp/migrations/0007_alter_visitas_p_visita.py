# Generated by Django 4.2.3 on 2023-10-05 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_visitas_h_salida_alter_visitas_h_termino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitas',
            name='p_visita',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='erp.trabajadores'),
        ),
    ]

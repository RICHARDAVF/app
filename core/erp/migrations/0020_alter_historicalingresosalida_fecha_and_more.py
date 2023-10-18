# Generated by Django 4.2.3 on 2023-10-18 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0019_alter_historicalingresosalida_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalingresosalida',
            name='fecha',
            field=models.DateField(blank=True, editable=False, null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='historicalingresosalida',
            name='hora',
            field=models.TimeField(blank=True, editable=False, null=True, verbose_name='Hora de salida'),
        ),
        migrations.AlterField(
            model_name='historicalingresosalida',
            name='tipo',
            field=models.CharField(choices=[('1', 'INGRESO'), ('2', 'SALIDA')], max_length=15),
        ),
        migrations.AlterField(
            model_name='ingresosalida',
            name='fecha',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='ingresosalida',
            name='hora',
            field=models.TimeField(auto_now_add=True, null=True, verbose_name='Hora de salida'),
        ),
        migrations.AlterField(
            model_name='ingresosalida',
            name='tipo',
            field=models.CharField(choices=[('1', 'INGRESO'), ('2', 'SALIDA')], max_length=15),
        ),
    ]

# Generated by Django 4.2.3 on 2023-10-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitas',
            name='h_llegada',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora de llegada'),
        ),
    ]
# Generated by Django 4.2.3 on 2023-11-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0025_alter_historicalvisitas_fv_soat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalparqueo',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='parqueo',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]

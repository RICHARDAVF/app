# Generated by Django 4.2.3 on 2023-09-15 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=150, verbose_name='Ubicacon')),
            ],
            options={
                'verbose_name': 'unidad',
                'verbose_name_plural': 'unidaddes',
                'db_table': 'unidades',
            },
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.CharField(max_length=15, verbose_name='Puesto')),
                ('direccion', models.CharField(max_length=150, verbose_name='Direccion')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.unidad', verbose_name='Modulo')),
            ],
            options={
                'verbose_name': 'puesto',
                'verbose_name_plural': 'puestos',
                'db_table': 'puestos',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='puesto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.puesto', verbose_name='Puesto'),
        ),
        migrations.AddField(
            model_name='user',
            name='unidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.unidad', verbose_name='Unidad'),
        ),
    ]

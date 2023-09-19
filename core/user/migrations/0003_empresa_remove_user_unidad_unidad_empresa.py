# Generated by Django 4.2.3 on 2023-09-18 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_unidad_puesto_user_puesto_user_unidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=11, unique=True, verbose_name='RUC')),
                ('razon_social', models.CharField(max_length=150, verbose_name='Razon social')),
            ],
            options={
                'verbose_name': 'empresa',
                'verbose_name_plural': 'empresas',
                'db_table': 'empresas',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='unidad',
        ),
        migrations.AddField(
            model_name='unidad',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.empresa'),
        ),
    ]
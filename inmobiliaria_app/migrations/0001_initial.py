# Generated by Django 5.0.4 on 2024-04-23 02:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inmobiliaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=100)),
                ('inmobiliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietarios', to='inmobiliaria_app.inmobiliaria')),
            ],
        ),
        migrations.CreateModel(
            name='Finca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('area_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_terreno', models.CharField(max_length=100)),
                ('inmobiliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fincas', to='inmobiliaria_app.inmobiliaria')),
                ('propietarios', models.ManyToManyField(related_name='fincas_propiedad', to='inmobiliaria_app.propietario')),
            ],
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('numero_pisos', models.IntegerField()),
                ('numero_apartamentos', models.IntegerField()),
                ('numero_habitaciones', models.IntegerField()),
                ('inmobiliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edificios', to='inmobiliaria_app.inmobiliaria')),
                ('propietarios', models.ManyToManyField(related_name='edificios_propiedad', to='inmobiliaria_app.propietario')),
            ],
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localidad', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('numero_habitaciones', models.IntegerField()),
                ('area_terreno', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inmobiliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='casas', to='inmobiliaria_app.inmobiliaria')),
                ('propietarios', models.ManyToManyField(related_name='casas_propiedad', to='inmobiliaria_app.propietario')),
            ],
        ),
    ]

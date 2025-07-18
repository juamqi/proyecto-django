# Generated by Django 5.2.4 on 2025-07-10 15:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaRutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(choices=[('LU', 'Lunes'), ('MA', 'Martes'), ('MI', 'Miércoles'), ('JU', 'Jueves'), ('VI', 'Viernes'), ('SA', 'Sábado'), ('DO', 'Domingo')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='ejercicios/imagenes/')),
                ('video_url', models.URLField(blank=True, null=True)),
                ('creado_por_usuario', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EjercicioDia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.PositiveIntegerField()),
                ('repeticiones', models.PositiveIntegerField()),
                ('peso_sugerido', models.FloatField(blank=True, null=True)),
                ('orden', models.PositiveIntegerField()),
                ('dia_rutina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ejercicios', to='app_rutina.diarutina')),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_rutina.ejercicio')),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('activa', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Progreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('series_realizadas', models.PositiveIntegerField()),
                ('reps_realizadas', models.PositiveIntegerField()),
                ('peso_usado', models.FloatField(blank=True, null=True)),
                ('comentarios', models.TextField(blank=True)),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_rutina.ejercicio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rutina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_rutina.rutina')),
            ],
        ),
        migrations.AddField(
            model_name='diarutina',
            name='rutina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dias', to='app_rutina.rutina'),
        ),
    ]

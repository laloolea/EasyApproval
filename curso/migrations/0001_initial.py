# Generated by Django 3.0 on 2019-12-11 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('duracion', models.SmallIntegerField(blank=True, null=True)),
                ('fecha_inicial', models.DateField(blank=True, null=True)),
                ('fecha_final', models.DateField(blank=True, null=True)),
                ('financiamiento', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('costo', models.FloatField(blank=True, null=True)),
                ('aula', models.CharField(blank=True, max_length=40, null=True)),
                ('cupo_min', models.SmallIntegerField(blank=True, null=True)),
                ('cupo_max', models.SmallIntegerField(blank=True, null=True)),
                ('estado', models.SmallIntegerField(choices=[(0, 'Planeación'), (1, 'En proceso de aprobación'), (2, 'Aprobado'), (3, 'Comenzado'), (4, 'Terminado')], default=0)),
                ('division', models.CharField(max_length=60)),
                ('departamento', models.CharField(max_length=40)),
                ('caracter', models.CharField(default='', max_length=150)),
                ('obj_general', models.TextField(blank=True, null=True)),
                ('obj_particular', models.TextField(blank=True, null=True)),
                ('contenido_sintetico', models.TextField(blank=True, null=True)),
                ('estilo_enseñanza', models.TextField(blank=True, null=True)),
                ('req_evaluacion', models.TextField(blank=True, null=True)),
                ('bibliografia', models.TextField(blank=True, null=True)),
                ('perfil_academico', models.TextField(blank=True, null=True)),
                ('utilidad_programa', models.TextField(blank=True, null=True)),
                ('experiencia', models.TextField(blank=True, null=True)),
                ('hab_alumnos', models.TextField(blank=True, null=True)),
                ('idioma', models.CharField(blank=True, max_length=50, null=True)),
                ('infraestructura', models.CharField(blank=True, max_length=200, null=True)),
                ('cargo_instructor', models.CharField(blank=True, max_length=50, null=True)),
                ('dependencia', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('correo', models.CharField(blank=True, max_length=35, null=True)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Profile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media/constancias/')),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.Curso')),
            ],
        ),
    ]

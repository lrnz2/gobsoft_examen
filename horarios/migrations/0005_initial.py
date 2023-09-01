# Generated by Django 4.2.4 on 2023-08-28 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('horarios', '0004_alter_clasehasdia_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('matricula', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('matricula', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('clave', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('creditos', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(max_length=5)),
                ('subgrupo', models.CharField(max_length=2)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horarios.docente')),
            ],
            options={
                'unique_together': {('grado', 'subgrupo', 'docente')},
            },
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.CharField(max_length=15)),
                ('dia', models.CharField(max_length=10)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='horarios.docente')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='horarios.materia')),
            ],
            options={
                'unique_together': {('materia', 'hora', 'dia')},
            },
        ),
        migrations.CreateModel(
            name='EstudianteHasGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horarios.estudiante')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horarios.grupo')),
            ],
            options={
                'unique_together': {('estudiante', 'grupo')},
            },
        ),
        migrations.CreateModel(
            name='ClaseHasGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horarios.clase')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horarios.grupo')),
            ],
            options={
                'unique_together': {('clase', 'grupo')},
            },
        ),
    ]
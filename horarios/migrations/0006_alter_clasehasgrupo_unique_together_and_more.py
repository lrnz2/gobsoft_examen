# Generated by Django 4.2.4 on 2023-08-29 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horarios', '0005_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='clasehasgrupo',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='clasehasgrupo',
            name='clase',
        ),
        migrations.RemoveField(
            model_name='clasehasgrupo',
            name='grupo',
        ),
        migrations.AlterUniqueTogether(
            name='estudiantehasgrupo',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='estudiantehasgrupo',
            name='estudiante',
        ),
        migrations.RemoveField(
            model_name='estudiantehasgrupo',
            name='grupo',
        ),
        migrations.AlterUniqueTogether(
            name='grupo',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='docente',
        ),
        migrations.DeleteModel(
            name='Clase',
        ),
        migrations.DeleteModel(
            name='ClaseHasGrupo',
        ),
        migrations.DeleteModel(
            name='Docente',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='EstudianteHasGrupo',
        ),
        migrations.DeleteModel(
            name='Grupo',
        ),
        migrations.DeleteModel(
            name='Materia',
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-15 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horarios', '0003_remove_alumnos_por_maestro_materia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos_por_maestro',
            name='alumno',
            field=models.ForeignKey( on_delete=django.db.models.deletion.DO_NOTHING, to='horarios.alumno'),
        ),
    ]

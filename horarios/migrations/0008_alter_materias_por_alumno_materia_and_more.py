# Generated by Django 4.2.4 on 2023-08-15 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horarios', '0007_alter_materias_por_maestro_materia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materias_por_alumno',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='horarios.materia'),
        ),
        migrations.AlterField(
            model_name='materias_por_maestro',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='horarios.materia'),
        ),
    ]

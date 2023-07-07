# Generated by Django 4.2 on 2023-07-07 03:03

import aplicacion.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0012_remove_usuario_direccion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compraboleto',
            old_name='f_compra',
            new_name='fecha',
        ),
        migrations.AlterField(
            model_name='compraboleto',
            name='horario',
            field=models.IntegerField(choices=[(1, '10:00 AM'), (2, '12:00 PM'), (3, '2:00 PM'), (4, '4:00 PM'), (5, '6:00 PM')]),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rut',
            field=models.CharField(error_messages='Debe ingresar rut', max_length=10, primary_key=True, serialize=False, validators=[aplicacion.models.rut_validator]),
        ),
    ]
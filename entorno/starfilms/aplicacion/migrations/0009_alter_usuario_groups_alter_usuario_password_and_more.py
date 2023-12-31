# Generated by Django 4.2 on 2023-07-06 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('aplicacion', '0008_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='Los grupos a los que pertenece el usuario.', related_name='usuarios_relacionados', to='auth.group', verbose_name='grupos'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Los permisos específicos de usuario.', related_name='usuarios_relacionados', to='auth.permission', verbose_name='permisos del usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]

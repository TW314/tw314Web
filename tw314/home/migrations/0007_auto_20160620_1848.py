# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 21:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_usuario_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='pais',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='perfil',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Perfil'),
        ),
    ]
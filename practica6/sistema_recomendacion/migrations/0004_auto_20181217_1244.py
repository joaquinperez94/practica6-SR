# Generated by Django 2.1.3 on 2018-12-17 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_recomendacion', '0003_auto_20181217_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntuacion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 17, 12, 44, 19, 74258)),
        ),
    ]

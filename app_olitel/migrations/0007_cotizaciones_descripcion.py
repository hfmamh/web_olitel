# Generated by Django 4.2 on 2023-05-29 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_olitel', '0006_cotizaciones_codigo_cotizaciones_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizaciones',
            name='descripcion',
            field=models.DateTimeField(null=True),
        ),
    ]

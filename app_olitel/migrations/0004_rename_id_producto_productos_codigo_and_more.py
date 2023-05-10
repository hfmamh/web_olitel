# Generated by Django 4.2 on 2023-05-09 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_olitel', '0003_alter_productos_id_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='id_producto',
            new_name='codigo',
        ),
        migrations.AddField(
            model_name='productos',
            name='categoria',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='productos',
            name='unidad',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
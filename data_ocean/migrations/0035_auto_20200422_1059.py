# Generated by Django 2.0.9 on 2020-04-22 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_ocean', '0034_auto_20200421_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='code',
            field=models.CharField(max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='kzed',
            name='code',
            field=models.CharField(max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='kzed',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]
# Generated by Django 3.1.8 on 2021-07-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0137_auto_20210704_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='amount of income', max_digits=12, null=True, verbose_name='amount'),
        ),
    ]

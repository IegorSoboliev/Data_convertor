# Generated by Django 3.1.8 on 2021-05-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0103_auto_20210518_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Salary'), (2, 'Interest'), (3, 'Dividends'), (4, 'From sale of property'), (5, 'From sale of securities or corporate rights'), (10, 'Other')], help_text='type of income', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='liability',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Loan'), (10, 'Other')], help_text='type of liability', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='luxuryitem',
            name='producer',
            field=models.TextField(blank=True, default='', help_text='producer of the item', verbose_name='producer'),
        ),
        migrations.AlterField(
            model_name='luxuryitem',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Art'), (2, 'Personal or home electronic devices'), (3, 'Antiques'), (4, 'Clothes'), (5, 'Jewelry'), (10, 'Other')], help_text='type of the item', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='luxuryitemright',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ownership'), (2, 'Beneficial ownership'), (3, 'Joint ownership'), (4, 'Common property'), (5, 'Rent'), (6, 'Usage'), (10, 'Other right of usage'), (7, 'Owner is another person'), (8, 'Family member did not provide the information')], help_text='type of the right', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'House'), (2, 'Summer house'), (3, 'Apartment'), (4, 'Room'), (5, 'Garage'), (6, 'Unfinished construction'), (7, 'Land'), (8, 'Office'), (10, 'Other')], help_text='type of the property', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='propertyright',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ownership'), (2, 'Beneficial ownership'), (3, 'Joint ownership'), (4, 'Common property'), (5, 'Rent'), (6, 'Usage'), (10, 'Other right of usage'), (7, 'Owner is another person'), (8, 'Family member did not provide the information')], help_text='type of the right', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='securities',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Share'), (2, 'Corporate right'), (10, 'Other')], help_text='type of securities', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='securitiesright',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ownership'), (2, 'Beneficial ownership'), (3, 'Joint ownership'), (4, 'Common property'), (5, 'Rent'), (6, 'Usage'), (10, 'Other right of usage'), (7, 'Owner is another person'), (8, 'Family member did not provide the information')], help_text='type of the right', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='vehicleright',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ownership'), (2, 'Beneficial ownership'), (3, 'Joint ownership'), (4, 'Common property'), (5, 'Rent'), (6, 'Usage'), (10, 'Other right of usage'), (7, 'Owner is another person'), (8, 'Family member did not provide the information')], help_text='type of the right', verbose_name='type'),
        ),
    ]

# Generated by Django 3.0.7 on 2021-05-06 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location_register', '0022_auto_20210415_0936'),
        ('business_register', '0094_auto_20210430_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='declaration',
            name='registration_address',
        ),
        migrations.RemoveField(
            model_name='declaration',
            name='residence_address',
        ),
        migrations.AddField(
            model_name='declaration',
            name='city_of_registration',
            field=models.ForeignKey(blank=True, default=None, help_text='city where the PEP is registered', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='declared_pep_registration', to='location_register.RatuCity', verbose_name='city of registration'),
        ),
        migrations.AddField(
            model_name='declaration',
            name='city_of_residence',
            field=models.ForeignKey(blank=True, default=None, help_text='city where the PEP lives', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='declared_pep_residence', to='location_register.RatuCity', verbose_name='city of residence'),
        ),
        migrations.AlterField(
            model_name='declaration',
            name='nacp_declarant_id',
            field=models.PositiveIntegerField(db_index=True, verbose_name='NACP id of the declarant'),
        ),
    ]

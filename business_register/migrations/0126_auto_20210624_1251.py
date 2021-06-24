# Generated by Django 3.1.8 on 2021-06-24 12:51

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location_register', '0024_auto_20210526_0845'),
        ('business_register', '0125_merge_20210624_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='declaration',
            name='beneficiary_of',
        ),
        migrations.AlterField(
            model_name='corporaterights',
            name='company_type_name',
            field=models.TextField(blank=True, default='', help_text='name of type of the company', verbose_name='name of type of the company'),
        ),
        migrations.AlterField(
            model_name='ngoparticipation',
            name='pep',
            field=models.ForeignKey(help_text='politically exposed person that participates in the NGO', on_delete=django.db.models.deletion.PROTECT, related_name='ngos', to='business_register.pep', verbose_name='PEP that participates in the NGO'),
        ),
        migrations.AlterField(
            model_name='personsanction',
            name='passports',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex='^[A-ZА-ЯЄЇҐІ0-9]+$')]), blank=True, default=list, size=None, verbose_name='passports'),
        ),
        migrations.CreateModel(
            name='Beneficary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the object was created. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='When the object was update. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.', null=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('company_name', models.TextField(blank=True, default='', help_text='name of the company', max_length=75, verbose_name='name of the company')),
                ('company_name_eng', models.TextField(blank=True, default='', help_text='name in English of the company', max_length=75, verbose_name='name of the company in English')),
                ('company_type_name', models.TextField(blank=True, default='', help_text='name of type of the company', verbose_name='name of type of the company')),
                ('company_phone', models.CharField(blank=True, default='', help_text='phone number of the company', max_length=25, verbose_name='phone number of the company')),
                ('company_fax', models.CharField(blank=True, default='', help_text='fax number of the company', max_length=25, verbose_name='fax number of the company')),
                ('company_email', models.CharField(blank=True, default='', help_text='email of the company', max_length=55, verbose_name='email of the company')),
                ('company_address', models.TextField(blank=True, default='', help_text='address of the company', verbose_name='address of the company')),
                ('company_registration_number', models.CharField(blank=True, default='', help_text='number of registration of the company', max_length=20, verbose_name='registration number of the company')),
                ('company', models.ForeignKey(blank=True, default=None, help_text='company', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='beneficiaries_from_declarations', to='business_register.company', verbose_name='company')),
                ('country', models.ForeignKey(blank=True, default=None, help_text='country where the company is registered', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='declared_pep_beneficiaries', to='location_register.country', verbose_name='country')),
                ('declaration', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='beneficiaries', to='business_register.declaration', verbose_name='declaration')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
    ]

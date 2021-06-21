# Generated by Django 3.1.8 on 2021-06-18 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0120_auto_20210615_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='NgoParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the object was created. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='When the object was update. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.', null=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('participation_type', models.PositiveSmallIntegerField(choices=[(1, 'Membership'), (2, 'Leadership')], help_text='type of the participation in the NGO', verbose_name='participation type')),
                ('ngo_type', models.PositiveSmallIntegerField(choices=[(1, 'Professional union'), (2, 'Public association'), (3, 'Charity')], help_text='type of the NGO', verbose_name='NGO type')),
                ('ngo_name', models.TextField(blank=True, default='', help_text='name of the NGO', verbose_name='NGO name')),
                ('ngo_registration_number', models.CharField(blank=True, default='', help_text='number of registration of the NGO', max_length=25, verbose_name='NGO registration number')),
                ('ngo_body_type', models.PositiveSmallIntegerField(choices=[(1, 'Audit body'), (2, 'Supervisory body'), (3, 'Governing body')], help_text='type of the NGO`s body', null=True, verbose_name='NGO body type')),
                ('ngo_body_name', models.TextField(blank=True, default='', help_text='name of the NGO`s body', verbose_name='NGO`s body name')),
                ('declaration', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ngo_participation', to='business_register.declaration', verbose_name='declaration')),
                ('ngo', models.ForeignKey(blank=True, default=None, help_text='NGO in which PEP participates', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='participants_peps', to='business_register.company', verbose_name='NGO')),
                ('pep', models.ForeignKey(help_text='politically exposed person that participates in the NGO', on_delete=django.db.models.deletion.PROTECT, related_name='ngo', to='business_register.pep', verbose_name='PEP that has the liability')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
    ]

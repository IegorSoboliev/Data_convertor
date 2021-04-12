# Generated by Django 3.1.7 on 2021-04-08 12:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0045_auto_20210407_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('should_complete_count', models.SmallIntegerField(default=0)),
                ('was_complete_count', models.SmallIntegerField(default=0)),
                ('was_overdue_count', models.SmallIntegerField(default=0)),
                ('was_overdue_grace_period_count', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_registration_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='payment registration date'),
            preserve_default=False,
        ),
    ]
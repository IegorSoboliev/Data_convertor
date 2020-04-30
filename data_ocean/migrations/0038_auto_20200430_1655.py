# Generated by Django 2.0.9 on 2020-04-30 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_ocean', '0037_auto_20200423_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_ocean.Category'),
        ),
        migrations.AddField(
            model_name='citydistrict',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_ocean.Category'),
        ),
    ]
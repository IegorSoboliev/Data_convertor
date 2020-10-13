# Generated by Django 3.0.7 on 2020-10-05 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0042_auto_20200915_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedPersonLinkWithPep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('relationship_type', models.CharField(max_length=90, null=True, verbose_name="тип зв'язку із публічним діячем")),
                ('relationship_type_eng', models.CharField(max_length=90, null=True, verbose_name="тип зв'язку із публічним діячем англійською")),
                ('start_date', models.CharField(max_length=12, null=True, verbose_name="дата виникнення зв'язку із публічним діячем")),
                ('confirmation_date', models.CharField(max_length=12, null=True, verbose_name="дата підтвердження зв'язку із публічним діячем")),
                ('end_date', models.CharField(max_length=12, null=True, verbose_name="дата припинення зв'язку із публічним діячем")),
                ('pep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pep_related_persons', to='business_register.Pep', verbose_name="публічний діяч, з яким ідентифікований зв'язок")),
                ('related_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_register.Pep', verbose_name="пов'язана з публічним діячем особа")),
            ],
            options={
                'verbose_name': "пов'язана з публічним діячем особа",
                'ordering': ['id'],
            },
        ),
    ]
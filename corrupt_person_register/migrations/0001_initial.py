# Generated by Django 3.1.7 on 2021-04-08 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityShpere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the object was created. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='When the object was update. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.', null=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('nazk_id', models.PositiveIntegerField(help_text='Identifier of the sphere of activity of an individual at the time of the offense', unique=True, verbose_name='NAZK id')),
                ('name', models.CharField(help_text='Name of the sphere of activity of an  individual at the time of the offense.', max_length=200, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Activity sphere',
            },
        ),
        migrations.CreateModel(
            name='CorruptCodexArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the object was created. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='When the object was update. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.', null=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('nazk_id', models.PositiveIntegerField(help_text='Identifier of the article according to which the person was prosecuted.', unique=True, verbose_name='NAZK id')),
                ('name', models.TextField(help_text='The name of the article under which the person was prosecuted.', verbose_name='name')),
            ],
            options={
                'verbose_name': 'Codex articles',
            },
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the object was created. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='When the object was update. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.', null=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('nazk_id', models.PositiveIntegerField(help_text='Identifier of court.', unique=True, verbose_name='NAZK id')),
                ('name', models.CharField(help_text='The name of the court.', max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Court',
            },
        ),
        migrations.CreateModel(
            name='LegalForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the object was created. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='When the object was update. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.', null=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('nazk_id', models.PositiveIntegerField(help_text='Identifier of organizational and legal form of ownership of a legal entity.', unique=True, verbose_name='NAZK id')),
                ('name', models.CharField(help_text='The name of the organizational and legal form of ownership of the legal entity.', max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Organizational and legal form',
            },
        ),
        migrations.CreateModel(
            name='Offense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the object was created. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='When the object was update. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.', null=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('nazk_id', models.PositiveIntegerField(help_text='Identifier of the corruption offense.', unique=True, verbose_name='NAZK id')),
                ('name', models.TextField(help_text='The name of the composition of the corruption offense / Method of imposing a disciplinary process.', verbose_name='name')),
            ],
            options={
                'verbose_name': 'Corruption offense',
            },
        ),
        migrations.CreateModel(
            name='CorruptPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the object was created. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='When the object was update. In YYYY-MM-DDTHH:mm:ss.SSSSSSZ format.', null=True)),
                ('deleted_at', models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True)),
                ('person_nazk_id', models.PositiveIntegerField(help_text='Identifier of the person in the NAZK database.', unique=True, verbose_name='NAZK id')),
                ('punishment_type', models.CharField(blank=True, choices=[('CD', 'Court decision'), ('DA', 'Disciplinary action')], help_text="Punishment type. Can be 'Court decision' or 'Disciplinary action'.", max_length=2, null=True, verbose_name='punishment type')),
                ('entity_type', models.CharField(blank=True, choices=[('I', 'Individual'), ('LE', 'Legal entity')], help_text="Entity type. Can be 'Individual' or 'Legal entity'.", max_length=2, null=True, verbose_name='entity type')),
                ('last_name', models.CharField(blank=True, db_index=True, help_text='The last name of the individual at the time of the offense.', max_length=30, null=True, verbose_name='last name')),
                ('first_name', models.CharField(blank=True, db_index=True, help_text='The name of the individual at the time of the offense.', max_length=20, null=True, verbose_name='first name')),
                ('middle_name', models.CharField(blank=True, db_index=True, help_text='The middle name of the individual at the time of the offense.', max_length=25, null=True, verbose_name='middle name')),
                ('place_of_work', models.CharField(blank=True, help_text='Place of work of an individual at the time of the offense.', max_length=350, null=True, verbose_name='place of work')),
                ('position', models.CharField(blank=True, help_text='Position of an  individual at the time of the offense.', max_length=100, null=True, verbose_name='position')),
                ('addr_post_index', models.CharField(blank=True, help_text='Address of registration of a legal entity at the time of the offense: postal code.', max_length=50, null=True, verbose_name='postcode')),
                ('addr_country_id', models.PositiveIntegerField(blank=True, help_text='Address of registration of a legal entity at the time of law enforcement: country identifier.', null=True, verbose_name='country identifier')),
                ('addr_country_name', models.CharField(blank=True, help_text='Address of registration of a legal entity at the time of the offense: name of the country.', max_length=50, null=True, verbose_name='country')),
                ('addr_state_id', models.PositiveIntegerField(blank=True, help_text='The address of registration of the legal entity at the time of the offense: the identifier of the region/city of national importance.', null=True, verbose_name='the identifier of the region/city')),
                ('addr_state_name', models.CharField(blank=True, help_text='The address of registration of the legal entity at the time of the offense: the name of the region/city of national importance', max_length=50, null=True, verbose_name='the name of the region/city')),
                ('addr_str', models.CharField(blank=True, help_text='The address of registration of the legal entity at the time of the offense: district, town, street, house, premises in the form of a line.', max_length=200, null=True, verbose_name='full address')),
                ('short_name', models.CharField(blank=True, db_index=True, help_text='Abbreviated name of the legal entity at the time of the offense.', max_length=20, null=True, verbose_name='short name of the legal entity')),
                ('legal_entity_name', models.CharField(blank=True, db_index=True, help_text='The name of the legal entity at the time of the offense.', max_length=50, null=True, verbose_name='the name of the legal entity')),
                ('registration_number', models.CharField(blank=True, db_index=True, help_text='EDRPOU code of the legal entity.', max_length=15, null=True, verbose_name='EDRPOU')),
                ('punishment', models.TextField(blank=True, default='data are missing.', help_text='The essence of satisfaction of claims / Type of disciplinary action.', null=True, verbose_name='punishment')),
                ('decree_date', models.DateField(blank=True, help_text='Date in YYYY-MM-DD format. Date of the order on imposition of disciplinary sanction.', null=True, verbose_name='decree date')),
                ('decree_number', models.CharField(blank=True, help_text='The number of the order imposing a disciplinary sanction.', max_length=20, null=True, verbose_name='decree number')),
                ('court_case_number', models.CharField(blank=True, help_text='The number of court case.', max_length=20, null=True, verbose_name='court case number')),
                ('sentence_date', models.DateField(blank=True, help_text='Date in YYYY-MM-DD format. Date of court decision.', null=True, verbose_name='sentence date')),
                ('sentence_number', models.CharField(blank=True, help_text='The number of court decision.', max_length=20, null=True, verbose_name='sentence number')),
                ('punishment_start', models.DateField(blank=True, help_text='Date in YYYY-MM-DD format. Date of entry into force of the court decision.', null=True, verbose_name='punishment start')),
                ('activity_sphere', models.ForeignKey(blank=True, help_text='The sphere of activity of an individual at the time of the offense.', null=True, on_delete=django.db.models.deletion.CASCADE, to='corrupt_person_register.activityshpere', verbose_name='activity sphere')),
                ('codex_articles', models.ManyToManyField(default='no data', help_text='The article under which the person was prosecuted.', to='corrupt_person_register.CorruptCodexArticle', verbose_name='codex articles')),
                ('court', models.ForeignKey(blank=True, help_text='The court that made the judgment.', null=True, on_delete=django.db.models.deletion.CASCADE, to='corrupt_person_register.court', verbose_name='court')),
                ('legal_form', models.ForeignKey(blank=True, help_text='The organizational and legal form of ownership of the legal entity.', null=True, on_delete=django.db.models.deletion.CASCADE, to='corrupt_person_register.legalform', verbose_name='legal form')),
                ('offense', models.ForeignKey(blank=True, help_text='The composition of the corruption offense / Method of imposing a disciplinary process.', null=True, on_delete=django.db.models.deletion.CASCADE, to='corrupt_person_register.offense', verbose_name='offense')),
            ],
            options={
                'verbose_name': 'Persons who have committed corruption or corruption-related offenses',
            },
        ),
    ]

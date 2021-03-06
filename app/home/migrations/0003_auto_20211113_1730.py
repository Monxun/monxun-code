# Generated by Django 3.2.9 on 2021-11-14 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_holidayseventsmodel_oilmodel_samplesubmissionmodel_storesmodel_testmodel_trainmodel_transactionsmode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('data', models.JSONField()),
                ('song_file', models.FileField(upload_to='songs/')),
                ('midi_file', models.FileField(upload_to='midi/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('info', models.JSONField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='HolidaysEventsModel',
        ),
        migrations.DeleteModel(
            name='OilModel',
        ),
        migrations.DeleteModel(
            name='SampleSubmissionModel',
        ),
        migrations.DeleteModel(
            name='StoresModel',
        ),
        migrations.DeleteModel(
            name='TableBacktests',
        ),
        migrations.DeleteModel(
            name='TableCharts',
        ),
        migrations.DeleteModel(
            name='TableCompanyInfo',
        ),
        migrations.DeleteModel(
            name='TableCurrencyuInfo',
        ),
        migrations.DeleteModel(
            name='TableForecasts',
        ),
        migrations.DeleteModel(
            name='TableSongs',
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.DeleteModel(
            name='TrainModel',
        ),
        migrations.DeleteModel(
            name='TransactionsModel',
        ),
    ]

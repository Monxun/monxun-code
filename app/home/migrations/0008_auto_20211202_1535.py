# Generated by Django 3.2.9 on 2021-12-02 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20211202_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backtest',
            name='entry_level',
        ),
        migrations.RemoveField(
            model_name='backtest',
            name='entry_price',
        ),
        migrations.RemoveField(
            model_name='backtest',
            name='exit_level',
        ),
        migrations.RemoveField(
            model_name='backtest',
            name='exit_price',
        ),
    ]

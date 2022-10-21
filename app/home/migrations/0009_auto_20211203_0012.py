# Generated by Django 3.2.9 on 2021-12-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211202_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backtest',
            name='entry_base',
        ),
        migrations.RemoveField(
            model_name='backtest',
            name='entry_cross',
        ),
        migrations.RemoveField(
            model_name='backtest',
            name='entry_target',
        ),
        migrations.RemoveField(
            model_name='backtest',
            name='exit_base',
        ),
        migrations.RemoveField(
            model_name='backtest',
            name='exit_cross',
        ),
        migrations.RemoveField(
            model_name='backtest',
            name='exit_target',
        ),
        migrations.AddField(
            model_name='backtest',
            name='backtest_base',
            field=models.CharField(choices=[('rsi', 'RSI'), ('obv', 'OBV'), ('ma', '200-SMA')], default='rsi', max_length=200),
        ),
        migrations.AddField(
            model_name='backtest',
            name='backtest_entry',
            field=models.CharField(choices=[('rsi', 'RSI'), ('obv', 'OBV'), ('ma', '200-SMA')], default='rsi', max_length=200),
        ),
        migrations.AlterField(
            model_name='backtest',
            name='symbol',
            field=models.CharField(max_length=5),
        ),
    ]
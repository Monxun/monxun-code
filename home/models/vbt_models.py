from django.db import models

# VBT MODELS
# OPTION IN GUI
class Backtest(models.Model):

    ENTRY = (
        ('rsi', 'RSI'),
        ('obv', 'OBV'),
        ('ma', '200-SMA'),
    )

    EXIT = (
        ('rsi', 'RSI'),
        ('obv', 'OBV'),
        ('ma', '200-SMA'),
    )

    # FOREIGN KEY -> BACKTEST
    symbol = models.CharField(max_length=5)

    # ENTRY SIGNAL
    backtest_entry = models.CharField(max_length=200, choices=ENTRY, default='rsi')

    # EXIT SIGNAL
    backtest_base = models.CharField(max_length=200, choices=EXIT, default='rsi')

    # PARAMS
    init_cash = models.IntegerField() # INPUT FIELD

    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.datetime


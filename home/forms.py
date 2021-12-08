from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models.mus_models import Song
from .models.vbt_models import Backtest

###############################################################
# MUS FORMS

class SongSearchForm(forms.Form):

    title = forms.CharField(label='Song', max_length=100)
    artist = forms.CharField(label='Artist', max_length=100)
    
    class Meta:

        model = Song
        
        fields = ("title", "artist")


###############################################################
# VBT FORMS

class SymbolForm(forms.Form):

    symbol = forms.CharField(label='Symbol', max_length=12)
    
    class Meta:

        model = Backtest
        
        fields = ("symbol")


class BacktestForm(ModelForm):

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
    

    # ENTRY SIGNAL
    backtest_entry = forms.ChoiceField(choices=ENTRY) # INPUT FIELD REQUIRED

  
    # EXIT SIGNAL
    backtest_exit = forms.ChoiceField(choices=EXIT) # INPUT FIELD REQUIRED

    # PARAMS
    init_cash = forms.IntegerField() # INPUT FIELD REQUIRED
    
    
    class Meta:

        model = Backtest
        
        fields = (
            'backtest_entry',
            'backtest_exit',
            'init_cash',
        )
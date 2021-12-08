from rest_framework import serializers
from .models.vbt_models import Backtest

class BacktestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backtest
        fields = (
            
            'entry_base', 
            'entry_cross', 
            'entry_target', 
            'entry_level', 
            'entry_ma_window', 
            'entry_price', 
            'exit_base', 
            'exit_cross', 
            'exit_target',
            'exit_level',
            'exit_ma_window',
            'exit_price',

            'init_cash',
        )
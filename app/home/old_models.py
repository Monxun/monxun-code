from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

##################################################################
#HOME



# ##################################################################
# #BIZ

# # ADD THE OTHER BIZ DATA TABLES HERE (Perhaps use a generic method
# # and pass table as keyword argument)

# class TableCharts(models.Model):
#     biz_chart = models.FileField() # <- NOT SURE ABOUT THIS SHIT!
#     biz_json = models.JSONField() # <- NOT SURE ABOUT THIS SHIT!

#     class Meta:
#         managed = False
#         db_table = 'charts'


# class TableForecasts(models.Model):
#     forecast_chart = models.FileField() # <- NOT SURE ABOUT THIS SHIT!
#     forecast_json = models.JSONField() # <- NOT SURE ABOUT THIS SHIT!

#     class Meta:
#         managed = False
#         db_table = 'forecasts'


##################################################################
#MUS

# class TableSongs(models.Model):
#     song_name = models.CharField(max_length=255, null=False)
#     artist = models.CharField(max_length=255, null=False)
#     song_file = models.FileField() # <- NOT SURE ABOUT THIS SHIT!
#     song_analysis = models.JSONField() # <- NOT SURE ABOUT THIS SHIT!

#     class Meta:
#         managed = False
#         db_table = 'songs'


##################################################################
#VBT

# class TableBacktests(models.Model):
#     backtest_chart = models.FileField() # <- NOT SURE ABOUT THIS SHIT!
#     backtest_json = models.JSONField() # <- NOT SURE ABOUT THIS SHIT!

#     class Meta:
#         managed = False
#         db_table = 'backtests'


# class TableCompanyInfo(models.Model):
#     company_json = models.JSONField() # <- NOT SURE ABOUT THIS SHIT!

#     class Meta:
#         managed = False
#         db_table = 'company_info'


# class TableCurrencyuInfo(models.Model):
#     company_json = models.JSONField() # <- NOT SURE ABOUT THIS SHIT!

#     class Meta:
#         managed = False
#         db_table = 'currency_info'


##################################################################
#LOGS TO-DO: MAKE LOGS! UNCOMMENT LATER HER AND IN db_router.py

# class TableLogsMus(models.Model):
#     description = models.CharField(max_length=255, null=False)

#     class Meta:
#         managed = False
#         db_table = 'mus_logs'


# class TableLogsBiz(models.Model):
#     description = models.CharField(max_length=255, null=False)

#     class Meta:
#         managed = False
#         db_table = 'biz_logs'


# class TableLogsVbt(models.Model):
#     description = models.CharField(max_length=255, null=False)

#     class Meta:
#         managed = False
#         db_table = 'vbt_logs'
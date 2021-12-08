from .models import (
    # BIZ MODELS
    TableCharts,
    TableForecasts,
    #DATA
    HolidaysEventsModel,
    OilModel,
    SampleSubmissionModel,
    StoresModel,
    TestModel,
    TrainModel,
    TransactionsModel,


    # MUS MODELS
    TableSongs,
    # VBT MODELS
    TableBacktests,
    TableCompanyInfo,
    TableCurrencyuInfo,
    # SYMBOL MODELS

    # LOGS MODELS
#     TableLogsMus,
#     TableLogsBiz,
#     TableLogsVbt,

)
# (Uncomment)

# SCHEMA / MODELS LIST

BIZ_MODELS = [
    TableCharts, 
    TableForecasts,
    HolidaysEventsModel,
    OilModel,
    SampleSubmissionModel,
    StoresModel,
    TestModel,
    TrainModel,
    TransactionsModel,
    ]
MUS_MODELS = [
    TableSongs,
    ]
SYMBOL_MODELS = [

    ]
VBT_MODELS = [
    TableBacktests,
    TableCompanyInfo,
    TableCurrencyuInfo,
    ]
    
# LOGS_MODELS = [
#     TableLogsMus,
#     TableLogsBiz,
#     TableLogsVbt,
# ]
# (Uncomment)


class MyDBRouter(object):



    #BIZ
    ######################################
    def db_for_read(self, model, **hints):
        if model in BIZ_MODELS:
            return 'biz'
        return None

    def db_for_write(self, model, **hints):
        if model in BIZ_MODELS:
            return 'biz'
        return None


    #MUS
    ######################################
    def db_for_read(self, model, **hints):
        if model in MUS_MODELS:
            return 'mus'
        return None

    def db_for_write(self, model, **hints):
        if model in MUS_MODELS:
            return 'mus'
        return None


    #VBT
    ######################################
    def db_for_read(self, model, **hints):
        if model in VBT_MODELS:
            return 'vbt'
        return None

    def db_for_write(self, model, **hints):
        if model in VBT_MODELS:
            return 'vbt'
        return None


    #LOGS (Uncomment)
    ######################################
    # def db_for_read(self, model, **hints):
    #     if model in LOGS_MODELS:
    #         return 'logs'
    #     return None

    # def db_for_write(self, model, **hints):
    #     if model in LOGS_MODELS:
    #         return 'logs'
    #     return None
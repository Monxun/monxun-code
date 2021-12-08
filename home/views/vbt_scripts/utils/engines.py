# ENGINE CLASSES FOR USER ACCESS TO CORRESPONDING METHODS / API

class Engine:
    pass


class DB_Engine(Engine):
    def __init__(self):
        from db.db_model import *
        from db.db_worker import *


class ML_Engine(Engine):
    pass


class PLT_Engine(Engine):
    pass

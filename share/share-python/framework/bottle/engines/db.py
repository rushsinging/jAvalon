#-*- coding: utf-8 -*-
from bottle import cached_property
from sqlalchemy import create_engine
from bottle import default_app

from share.engines.db import DataBaseOperation


class TableOpt(object):
    def as_dict(self):
        return {}


class DataBaseOperation(DataBaseOperation):
    @cached_property
    def engine(self):
        app = default_app()
        return create_engine(
            app.config.db_master, echo=app.config.enable_sql_echo)


db = DataBaseOperation()
db.TableOpt = TableOpt

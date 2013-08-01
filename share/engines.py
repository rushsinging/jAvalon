#-*- coding: utf-8 -*-
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from bottle import default_app
from bottle import cached_property


class DataBaseOperation(object):
    @cached_property
    def Model(self):
        return declarative_base()

    @cached_property
    def engine(self):
        app = default_app()
        return create_engine(
            app.config.db_master, echo=app.config.enable_sql_echo)

    @cached_property
    def session(self):
        return scoped_session(sessionmaker(bind=self.engine))


db = DataBaseOperation()


class TableOpt(object):
    @classmethod
    def create(cls, *args, **kwargs):
        tmp = cls(*args, **kwargs)
        db.session.add(tmp)
        db.session.commit()
        return tmp

    def update(self):
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

    @classmethod
    def query(cls):
        return db.session.query(cls)

    def as_dict(self):
        return {}
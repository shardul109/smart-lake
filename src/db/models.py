from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Date, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

cdb = None
DBSession: sessionmaker = None
Base = declarative_base()


def init_db():
    global cdb, DBSession
    config_path = f'src/db'
    cdb = create_engine(
        f'sqlite:///{config_path}/config.db', connect_args={'check_same_thread': False})
    Base.metadata.create_all(cdb)
    Base.metadata.bind = cdb
    DBSession = sessionmaker(bind=cdb)


def get_session():
    if DBSession is not None:
        session = DBSession()
        return session
    else:
        return None


class DeviceValues(Base):
    __tablename__ = 'device_values'

    id = Column(Integer, primary_key=True)
    temperature = Column(Float)
    humidity = Column(Float)
    time = Column(DateTime)



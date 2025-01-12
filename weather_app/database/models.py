from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(100), nullable=False)  # Specify length for VARCHAR
    temperature = Column(Float, nullable=False)
    description = Column(String(255), nullable=False)  # Specify length for VARCHAR


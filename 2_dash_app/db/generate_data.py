from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///example.db")
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class SinusoidalData(Base):
    __tablename__ = "sinusoidal_data"
    id = Column(Integer, primary_key=True)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)

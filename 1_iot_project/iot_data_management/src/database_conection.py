from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# 1 - SQL statement to create a database table, but best to instantiate with sqlalchemy for reproducibility.
#CREATE TABLE sensor_data (
#    sensor_id INTEGER,
#    timestamp TEXT,
#    temperature REAL,
#    humidity INTEGER,
#    pressure INTEGER,
#    PRIMARY KEY (sensor_id, timestamp))

Base = declarative_base()

# Define the SensorData model
class SensorData(Base):
    
    __tablename__ = 'sensor_data'

    sensor_id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, primary_key=True)
    temperature = Column(Float)
    location =  Column(String)
    
    
    # Map columns:
    # e.g: id: Mapped[int]
    
    def __repr__(self) -> str:
        return f"sensor_id={self.sensor_id}"


    





from src.database_conection import SensorData
from sqlalchemy as sa
from sqlalchemy.orm import sessionmaker



if __name__ == "__main__":

    db = sa.create_engine("sqlite:///database/data_csv.db")
    Session = sessionmaker(bind=db)
    session = Session()
    
    # 
    for index, row in df.iterrows():


    SensorData
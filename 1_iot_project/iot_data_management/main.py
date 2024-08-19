from src.database_conection import SensorData, Base
from src.read_data import ReadFiles
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

DATABASE_PATH = r"C:\Users\carlo\Desktop\Repo\python_projects\1_iot_project\iot_data_management\database\database_csv.db"
DATA_CSV= r"C:\Users\carlo\Desktop\Repo\python_projects\1_iot_project\iot_data_management\data\MOCK_DATA.csv"


if __name__ == "__main__":

    db = create_engine(f"sqlite:///{DATABASE_PATH}")
    Session = sessionmaker(bind=db)
    session = Session()
    # Create all tables in the database
    Base.metadata.create_all(db)
    
    dataframe = ReadFiles(DATA_CSV).df
    # 
    for index, row in dataframe.iterrows():
        sensor_data = SensorData(
        sensor_id=row['sensor_id'],
        timestamp=row['timestamp'],
        temperature=row['temperature'],
        location=row['location'])
        
        session.add(sensor_data)
        
    session.add(sensor_data)
    
    # Fetch and print all table names in the database
    inspector = inspect(db)
    table_names = inspector.get_table_names()
    print(f"Tables in the database: {table_names}")

    # Fetch and print the columns of a specific table (e.g., 'sensor_data')
    for table_name in table_names:
        columns = inspector.get_columns(table_name)
        print(f"Columns in table '{table_name}': {[column['name'] for column in columns]}")


    # Close the session
    session.close()

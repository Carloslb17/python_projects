# Read data

import pandas as pd


class ReadFiles():
    """_summary_
        path: Introduce the path to read the data. 
    
    """
    def __init__(self, path) -> None:
        self.path = path
        
        if ".csv" in path:
            self.df = self.open_csv()
        
        
        
    def open_csv(self) -> pd.DataFrame:
        return pd.read_csv(self.path)
        
    
    
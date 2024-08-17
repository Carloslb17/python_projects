# Read data

import pandas as pd


class ReadFiles():
    def __init__(self, path) -> None:
        self.path = path
        
        if ".csv" in path:
            self.open_csv(self.path)
        
        
        
    def open_csv(self) -> pd.DataFrame:
        return pd.read_csv(self.path)
        
    
    
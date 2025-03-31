import pandas as pd
from abc import ABC, abstractmethod

class AbstractDataSource(ABC):
    @abstractmethod
    def get_dataframe(self) -> pd.DataFrame:
        pass

class CSVDataSource(AbstractDataSource):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_dataframe(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)

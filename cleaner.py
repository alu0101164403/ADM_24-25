import pandas as pd
from abc import ABC, abstractmethod

class AbstractCleaner(ABC):
    @abstractmethod
    def clean(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        pass

class GenericCleaner(AbstractCleaner):
    def __init__(self, 
                 cols_to_drop=None,
                 cols_required=None,
                 cols_fill_mean=None,
                 cols_fill_mode=None):
        self.cols_to_drop = cols_to_drop or []
        self.cols_required = cols_required or []
        self.cols_fill_mean = cols_fill_mean or []
        self.cols_fill_mode = cols_fill_mode or []

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        # Eliminar columnas
        df = df.drop(columns=self.cols_to_drop, errors='ignore')

        # Eliminar filas con valores nulos en columnas clave
        df = df.dropna(subset=self.cols_required)

        # Imputar columnas numéricas con la media
        for col in self.cols_fill_mean:
            if col in df.columns:
                df[col] = df[col].fillna(df[col].mean())

        # Imputar columnas categóricas con la moda
        for col in self.cols_fill_mode:
            if col in df.columns and not df[col].mode().empty:
                df[col] = df[col].fillna(df[col].mode()[0])

        return df

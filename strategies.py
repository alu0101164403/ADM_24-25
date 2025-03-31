import matplotlib.pyplot as plt
import seaborn as sns
from abc import ABC, abstractmethod
import pandas as pd

class VisualizationStrategy(ABC):
    @abstractmethod
    def plot(self, dataframe: pd.DataFrame):
        pass

class BarChartStrategy(VisualizationStrategy):
    def __init__(self, x: str, top_n: int = 10):
        self.x = x
        self.top_n = top_n

    def plot(self, df: pd.DataFrame):
        plt.figure(figsize=(10, 6))
        top_values = df[self.x].value_counts().head(self.top_n)
        sns.barplot(x=top_values.index, y=top_values.values)
        plt.title(f"Top {self.top_n} valores de {self.x}")
        plt.xlabel(self.x)
        plt.ylabel("Número de accidentes")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

class LineChartStrategy(VisualizationStrategy):
    def __init__(self, x: str, y: str):
        self.x = x
        self.y = y

    def plot(self, df: pd.DataFrame):
        df_sorted = df.sort_values(by=self.x)
        plt.figure(figsize=(10, 6))
        plt.plot(df_sorted[self.x], df_sorted[self.y], alpha=0.5)
        plt.title(f"{self.y} vs {self.x}")
        plt.xlabel(self.x)
        plt.ylabel(self.y)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

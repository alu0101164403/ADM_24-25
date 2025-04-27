import matplotlib.pyplot as plt
import seaborn as sns
from abc import ABC, abstractmethod
import pandas as pd

class VisualizationStrategy(ABC):
    @abstractmethod
    def plot(self, dataframe: pd.DataFrame, label: str = None):
        pass

class BarChartStrategy(VisualizationStrategy):
    def __init__(self, x: str, top_n: int = 20):
        self.x = x
        self.top_n = top_n

    def plot(self, df: pd.DataFrame, label: str = None):
        plt.figure(figsize=(10, 6))
        top_values = df[self.x].value_counts().head(self.top_n)
        sns.barplot(x=top_values.index, y=top_values.values)
        plt.title(f"Top {self.top_n} valores de {self.x}")
        plt.xlabel(self.x)
        plt.ylabel("Número de accidentes")
        plt.xticks(rotation=45)
        if label:
            plt.legend([label])
        plt.tight_layout()
        plt.show()

class LineChartStrategy(VisualizationStrategy):
    def __init__(self, x: str, y: str):
        self.x = x
        self.y = y

    def plot(self, df: pd.DataFrame, label: str = None):
        df_sorted = df.sort_values(by=self.x)
        plt.figure(figsize=(10, 6))
        plt.plot(df_sorted[self.x], df_sorted[self.y], alpha=0.5, label=label)
        plt.title(f"{self.y} vs {self.x}")
        plt.xlabel(self.x)
        plt.ylabel(self.y)
        plt.xticks(rotation=45)
        if label:
            plt.legend()
        plt.tight_layout()
        plt.show()

class ScatterStrategy(VisualizationStrategy):
    def __init__(self, x: str, y: str):
        self.x, self.y = x, y

    def plot(self, df: pd.DataFrame, label: str = None):
        plt.figure(figsize=(10, 6))
        plt.scatter(df[self.x], df[self.y], alpha=0.6, label=label)
        plt.title(f"{self.y} vs {self.x} (Scatter)")
        plt.xlabel(self.x)
        plt.ylabel(self.y)
        if label:
            plt.legend()
        plt.tight_layout()
        plt.show()

class HistogramStrategy(VisualizationStrategy):
    def __init__(self, x: str, bins: int = 20):
        self.x, self.bins = x, bins

    def plot(self, df: pd.DataFrame, label: str = None):
        plt.figure(figsize=(10, 6))
        plt.hist(df[self.x], bins=self.bins, alpha=0.6, label=label)
        plt.title(f"Histograma de {self.x}")
        plt.xlabel(self.x)
        plt.ylabel('Frecuencia')
        if label:
            plt.legend()
        plt.tight_layout()
        plt.show()


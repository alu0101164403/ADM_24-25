from strategies import VisualizationStrategy
import pandas as pd

class Visualizer:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: VisualizationStrategy):
        self.strategy = strategy

    def render(self, dataframe: pd.DataFrame):
        if self.strategy is None:
            raise Exception("No se ha definido una estrategia de visualización.")
        self.strategy.plot(dataframe)

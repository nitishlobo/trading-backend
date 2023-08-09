"""Module defining base strategies."""
from abc import ABC, abstractmethod

from pandas import DataFrame
from schemas.data_sources import DataColumns
from schemas.trading import CompletedTrade, TradeInterval


class Strategy(ABC):
    """Abstract class for strategy implementation."""

    @abstractmethod
    def get_profitable_trades(
        self,
        trade_data: DataFrame,
        data_cols: DataColumns,
        trade_interval: TradeInterval,
    ) -> list[CompletedTrade]:
        """Return profitable trades given a data set with time and price.

        Keyword arguments:
        trade_data -- object containing the time and price history of the share/stock/market.
        data_cols -- column names for trade data.
        trade_interval -- allowable min and max intervals between open and close trade times.
        """

"""Module defining abstract interface for strategies."""

from pandas import DataFrame
from schemas.data_sources import DataColumns
from schemas.trading import CompletedTrade, TradeInterval
from services.strategies.base import Strategy


class Context:
    """Strategy context which allows different trading strategies to be called."""

    def __init__(self, strategy: Strategy) -> None:
        """Initialise a trading strategy."""
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """Return reference to strategy object."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """Set strategy.

        Allows changing strategy at runtime as opposed to being intialised in the __init__.

        Keyword arguments:
        strategy -- strategy class which be used to get trades.
        """
        self._strategy = strategy

    def get_trades(
        self,
        trade_data: DataFrame,
        data_cols: DataColumns,
        trade_interval: TradeInterval,
    ) -> list[CompletedTrade]:
        """Return profits of trade transactions.

        Keyword arguments:
        trade_data -- object containing the time and price history of the share/stock/market.
        data_cols -- column names for trade data.
        trade_interval -- allowable min and max intervals between open and close trade times.
        """
        self.trades = self._strategy.get_profitable_trades(trade_data, data_cols, trade_interval)
        return self.trades

    def get_profits(
        self,
        trade_data: DataFrame,
        data_cols: DataColumns,
        trade_interval: TradeInterval,
    ) -> list[float]:
        """Return a list of all the profits made with each trade.

        Keyword arguments:
        trade_data -- object containing the time and price history of the share/stock/market.
        data_cols -- column names for trade data.
        trade_interval -- allowable min and max intervals between open and close trade times.
        """
        trades = self.get_trades(trade_data, data_cols, trade_interval)
        return [trade.closing.price - trade.opening.price for trade in trades]

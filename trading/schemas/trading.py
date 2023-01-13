"""Module defining data classes for trades."""
from settings import MIN_TRADE_TIME_IN_MINS, MAX_TRADE_TIME_IN_MINS
from schemas.base import TradingBase


class Trade(TradingBase):  # pylint: disable=too-few-public-methods
    """Holds information about a trade value for a specific time."""

    time: int
    price: float


class TradeInterval(TradingBase):  # pylint: disable=too-few-public-methods
    """Defines minimum and maximum time between open and close of a trade."""

    min_: int = MIN_TRADE_TIME_IN_MINS
    max_: int = MAX_TRADE_TIME_IN_MINS


class CompletedTrade(TradingBase):  # pylint: disable=too-few-public-methods
    """Holds information about a completed (bought and sold) trade transaction."""

    opening: Trade
    closing: Trade

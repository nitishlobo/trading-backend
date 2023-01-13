"""Module defining data classes for data sources."""
from settings import DEFAULT_PRICE_COL_NAME, DEFAULT_TIME_COL_NAME
from schemas.base import TradingBase


class DataColumns(TradingBase):  # pylint: disable=too-few-public-methods
    """Holds information about a trade data columns."""

    time: str = DEFAULT_TIME_COL_NAME
    price: str = DEFAULT_PRICE_COL_NAME

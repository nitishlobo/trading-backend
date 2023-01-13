"""Module for testing trading services."""
from typing import List

import pytest
from pandas import DataFrame

from trading.schemas.data_sources import DataColumns
from trading.schemas.trading import CompletedTrade, TradeInterval
from trading.services import trading as trading_services


@pytest.mark.parametrize(
    "min_interval, max_interval",
    [
        (0, 10),
        (4, 7),
        (5, 11),
        (19, 30),
    ],
)
def test_trade_being_able_to_close_a_trade(
    fixture_crypto_trade_data: DataFrame, min_interval: int, max_interval: int
) -> None:
    """Test is_trade_possible function when trades are possible."""
    data_cols = DataColumns()
    trade_interval = TradeInterval(min_=min_interval, max_=max_interval)
    should_trade = trading_services.is_trade_possible(
        fixture_crypto_trade_data, data_cols, trade_interval
    )
    assert should_trade is True


@pytest.mark.parametrize(
    "min_interval, max_interval",
    [
        (31, 44),
        (45, 52),
        (65, 76),
    ],
)
def test_not_being_able_to_close_a_trade(
    fixture_crypto_trade_data: DataFrame, min_interval: int, max_interval: int
) -> None:
    """Test is_trade_possiblewhen trades are not possible."""
    data_cols = DataColumns()
    trade_interval = TradeInterval(min_=min_interval, max_=max_interval)
    should_trade = trading_services.is_trade_possible(
        fixture_crypto_trade_data, data_cols, trade_interval
    )
    assert should_trade is False


def test_get_profitable_trades(
    fixture_crypto_trade_data: DataFrame,
    fixture_most_profitable_crypto_trades: List[CompletedTrade],
) -> None:
    """Test getting the most profitable trades from a data set."""
    data_cols = DataColumns()
    trade_interval = TradeInterval(min_=5, max_=30)
    trades = trading_services.get_profitable_trades(
        fixture_crypto_trade_data, data_cols, trade_interval
    )
    assert trades == fixture_most_profitable_crypto_trades


def test_get_profits(
    fixture_completed_medical_trades: List[CompletedTrade],
    fixture_medical_trade_profits: List[float],
) -> None:
    """Test get profits function."""
    profits = trading_services.get_profits(fixture_completed_medical_trades)
    assert profits == fixture_medical_trade_profits

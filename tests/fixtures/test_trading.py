"""Module defining fixtures for data sources."""
from typing import List

import pandas
import pytest
from pandas import DataFrame

from trading.schemas.trading import CompletedTrade, Trade
from tests.fixtures.test_data_sources import DATA_SOURCE_TEST_DIR


@pytest.fixture
def fixture_crypto_trade_data() -> DataFrame:
    """Return crypto trading data frame."""
    crypto_data_frame = pandas.read_csv(f"{DATA_SOURCE_TEST_DIR}/crypto_market.csv")
    return crypto_data_frame


@pytest.fixture
def fixture_most_profitable_crypto_trades() -> List[CompletedTrade]:
    """Return most profitable crypto trades."""
    return [CompletedTrade(opening=Trade(time=0, price=2), closing=Trade(time=20, price=99))]


@pytest.fixture
def fixture_completed_medical_trades() -> List[CompletedTrade]:
    """Return list of completed trades."""
    trades = [
        CompletedTrade(opening=Trade(time=0, price=10.0), closing=Trade(time=20, price=31.0)),
        CompletedTrade(opening=Trade(time=21, price=11.0), closing=Trade(time=40, price=57.0)),
        CompletedTrade(opening=Trade(time=41, price=45.0), closing=Trade(time=60, price=96.0)),
        CompletedTrade(opening=Trade(time=61, price=42.2), closing=Trade(time=80, price=77.9)),
    ]
    return trades


@pytest.fixture
def fixture_medical_trade_profits() -> List[float]:
    """Return list of completed trades."""
    return [21.0, 46.0, 51.0, 35.7]

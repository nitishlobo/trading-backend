"""Pytest default configuration file. This module contains all the fixtures."""
# pylint: disable=unused-import, wrong-import-position
import sys

# Allow module to be called individually
sys.path.append("./trading")

from tests.fixtures.test_data_sources import (
    fixture_data_source_paths,
    fixture_expected_csv_paths,
)
from tests.fixtures.test_trading import (
    fixture_crypto_trade_data,
    fixture_most_profitable_crypto_trades,
    fixture_completed_medical_trades,
    fixture_medical_trade_profits,
)

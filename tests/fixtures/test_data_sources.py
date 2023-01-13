"""Module defining fixtures for data sources."""
from pathlib import Path

import pytest


DATA_SOURCE_TEST_DIR = "tests/fixtures/data"


@pytest.fixture
def fixture_data_source_paths():
    """Define data source paths."""
    return [DATA_SOURCE_TEST_DIR]


@pytest.fixture
def fixture_expected_csv_paths():
    """Define expected  data sources."""
    expected_files = ["crypto_market.csv", "retaiL_market.csv"]
    expected_paths = [Path(f"{DATA_SOURCE_TEST_DIR}/{file_}") for file_ in expected_files]
    return expected_paths

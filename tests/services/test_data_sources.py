"""Module for testing data source services."""
from pathlib import PosixPath
from typing import List

from trading.services import data_sources as data_services


def test_get_csv_paths(
    fixture_data_source_paths: List[str], fixture_expected_csv_paths: List[PosixPath]
) -> None:
    """Test get csv paths function."""
    data_sources = data_services.get_csv_paths(fixture_data_source_paths)
    assert data_sources.sort() == fixture_expected_csv_paths.sort()

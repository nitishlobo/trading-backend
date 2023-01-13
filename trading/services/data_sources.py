"""Services for sourcing data."""
from pathlib import Path, PosixPath
from typing import List


def get_csv_paths(paths: List[str]) -> List[PosixPath]:
    """Gets CSV related data sources from a given path.

    Keyword arguments:
    paths -- paths to get CSV files from.
    """
    csv_paths = []
    for path in paths:
        csv_paths.extend(list(Path(path).glob("*.csv")))

    return csv_paths

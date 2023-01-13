"""Module for presenting data source options."""
from pathlib import PosixPath
from typing import List


def get_data_source_selection(paths: List[PosixPath]) -> PosixPath:
    """Display data sources to user and get user to select which one to use.

    paths -- list of paths to data source objects.
    """
    # Display all data sources
    for index, path in enumerate(paths):
        print(f"\t#ID {index} - {path.as_posix()}")

    # Keep asking user until user enters a valid selection
    selected_data_source = None
    max_id = len(paths) - 1
    while selected_data_source is None:
        try:
            data_source_id = int(input("\nPlease select a valid #ID: "))
            if data_source_id < 0 or data_source_id > max_id:
                raise IndexError
        except (ValueError, IndexError):
            print(f"Error: Please enter a valid value between 0 and {max_id}. Try again.")
        else:
            selected_data_source = paths[data_source_id]
            break

    return selected_data_source

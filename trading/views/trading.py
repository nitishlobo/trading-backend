"""Module for presenting trading outcomes."""
from typing import List

from schemas.trading import CompletedTrade


def display_trades(trades: List[CompletedTrade], profits: List[float]) -> None:
    """Display trades and profit information.

    Keyword arguments:
    trade -- list of time and price information for opening and closing trades.
    profits -- list of profits corresponding to the trades.
    """
    print("Trades are:")
    for index, trade in enumerate(trades):
        print(
            f"Open at {trade.opening.time} ({trade.opening.price}), close {trade.closing.time} ({trade.closing.price}) for profit {profits[index]}"
        )
    print(f"Total profit {sum(profits)}")

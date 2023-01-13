"""Module for trading algorithms."""
from typing import List

from pandas import DataFrame

from schemas.data_sources import DataColumns
from schemas.trading import CompletedTrade, Trade, TradeInterval


def is_trade_possible(
    trade_data: DataFrame, data_cols: DataColumns, trade_interval: TradeInterval
) -> bool:
    """Return True if a trade is possible with the given data set.
    I.e. the trade close time satisifes the min and max trade interval from the open trade time.

    Keyword arguments:
    trade_data -- object containing the time and price history of the share/stock/market.
    data_cols -- column names for trade data.
    trade_interval -- allowable min and max intervals between open and close trade times.
    """
    # No trades possible if incoming trade data is empty.
    if trade_data.empty:
        return False

    # Get opening trade
    data = trade_data.sort_values(by=[data_cols.time], ascending=True)
    opening_trade = data.head(1)
    open_time = opening_trade[data_cols.time].item()
    open_price = opening_trade[data_cols.price].item()

    # Check for time interval constraint
    min_trade_time = open_time + trade_interval.min_
    max_trade_time = open_time + trade_interval.max_
    possible_closings = data[data_cols.time].between(min_trade_time, max_trade_time)

    # Check selling price should be higher than buying constraint
    closing_trade = (
        data[possible_closings].sort_values(by=[data_cols.price], ascending=False).head(1)
    )
    if closing_trade.empty:
        return False

    close_time = closing_trade[data_cols.time].item()
    close_price = closing_trade[data_cols.price].item()
    is_within_time_interval = (
        (open_time - trade_interval.min_) <= close_time <= (open_time + trade_interval.max_)
    )
    return open_price < close_price and is_within_time_interval


def get_profitable_trades(  # pylint: disable=too-many-locals
    trade_data: DataFrame, data_cols: DataColumns, trade_interval: TradeInterval
) -> List[CompletedTrade]:
    """Return profitable trades given a data set with time and price.

    Keyword arguments:
    trade_data -- object containing the time and price history of the share/stock/market.
    data_cols -- column names for trade data.
    trade_interval -- allowable min and max intervals between open and close trade times.
    """
    # Make a copy of the original data set to avoid changing the original.
    data = trade_data.copy()

    # Get column names
    price_col = data_cols.price
    time_col = data_cols.time

    # Check whether data satisfies trade constraints
    should_trade = is_trade_possible(data, data_cols, trade_interval)

    trades = []
    while should_trade:
        # Get data sorted by lowest and highest
        data_by_lowest = data.sort_values(by=[price_col], ascending=True)
        data_by_highest = data.sort_values(by=[price_col], ascending=False)

        # Opening trade will the lowest.
        # Closing trade will be the highest in the allowed time interval.
        opening_trade = data_by_lowest.head(1)
        min_trade_time = opening_trade[time_col].item() + trade_interval.min_
        max_trade_time = opening_trade[time_col].item() + trade_interval.max_
        closing_trade = data_by_highest[
            data_by_highest[time_col].between(min_trade_time, max_trade_time)
        ].head(1)

        # Exit if closing trade is not possible
        if closing_trade.empty:
            break

        highest_index = closing_trade[time_col].index.item()
        data.drop(
            data.index[0 : data.index.get_loc(highest_index)],
            inplace=True,
        )

        # Record trade
        completed_trade = CompletedTrade(
            opening=Trade(
                time=opening_trade[time_col].item(), price=opening_trade[price_col].item()
            ),
            closing=Trade(
                time=closing_trade[time_col].item(), price=closing_trade[price_col].item()
            ),
        )
        trades.append(completed_trade)

        # Next iteration
        should_trade = is_trade_possible(data, data_cols, trade_interval)
    return trades


def get_profits(trades: List[CompletedTrade]) -> List[float]:
    """Return profits of a trade transactions.

    Keyword arguments:
    trade -- list of time and price information for opening and closing trades.
    """
    return [trade.closing.price - trade.opening.price for trade in trades]

"""App for finding the most profitable trades from a given data set."""
import pandas

from schemas.data_sources import DataColumns
from schemas.trading import TradeInterval
from services import data_sources as data_services
from services import trading as trading_services
from settings import CSV_DATA_PATHS
from views import data_sources as data_views
from views import trading as trading_views


def main():
    """Main trading app."""
    # Get data source to analyse
    csv_paths = data_services.get_csv_paths(CSV_DATA_PATHS)
    data_source = data_views.get_data_source_selection(csv_paths)
    trading_data_frame = pandas.read_csv(data_source.as_posix())

    # Remove empty data rows and duplicates
    trading_data_frame.dropna(inplace=True)
    trading_data_frame.drop_duplicates(inplace=True)

    # Get all completed trades (open and closed)
    data_cols = DataColumns()
    trade_interval = TradeInterval()
    trades = trading_services.get_profitable_trades(
        trading_data_frame,
        data_cols,
        trade_interval,
    )
    profits = trading_services.get_profits(trades)
    trading_views.display_trades(trades, profits)


if __name__ == "__main__":
    main()

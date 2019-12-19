import csv
from abc import abstractmethod
from functools import lru_cache
from typing import List

from super_simple_stocks.model import StockExchangeInfo
from super_simple_stocks.utils import convert_percentage_string_to_factor

_PAR_VALUE = 'Par Value'
_FIXED_DIVIDEND = 'Fixed Dividend'
_LAST_DIVIDEND = 'Last Dividend'
_TYPE = 'Type'
_STOCK_SYMBOL = 'Stock Symbol'
_EXPECTED_HEADER_COLUMNS = [_STOCK_SYMBOL, _TYPE, _LAST_DIVIDEND, _FIXED_DIVIDEND, _PAR_VALUE]


class Exchange:
    """
    Holds information about stocks relating to dividends and related metrics.
    """

    @abstractmethod
    def get_stock_data(self, stock_name) -> StockExchangeInfo:
        pass

    @abstractmethod
    def get_stock_names(self) -> StockExchangeInfo:
        pass


class FileExchange(Exchange):

    def __init__(self, csv_file_path_as_it_is_in_assignment):
        with open(csv_file_path_as_it_is_in_assignment) as csv_file:
            # Intended for small files
            header, *data_rows = list(csv.reader(csv_file))
            self._validate_header(header)
            self._exchange_info_repository = {
                self._get_column_value_from_row(row, _STOCK_SYMBOL): self._create_stock_info_from_row(row)
                for row in data_rows
            }

    @staticmethod
    def _validate_header(header):
        if not header == _EXPECTED_HEADER_COLUMNS:
            raise RuntimeError(
                f'The csv file you provided is invalid, columns need to be exactly: '
                f'[{",".join(_EXPECTED_HEADER_COLUMNS)}], but got [{",".join(header)}]'
            )

    def _create_stock_info_from_row(self, row):
        return StockExchangeInfo(
            stock_symbol=self._get_column_value_from_row(row, _STOCK_SYMBOL),
            type=self._get_column_value_from_row(row, _TYPE),
            last_dividend_per_share=int(self._get_column_value_from_row(row, _LAST_DIVIDEND)),
            fixed_dividend_factor=convert_percentage_string_to_factor(
                self._get_column_value_from_row(row, _FIXED_DIVIDEND)
            ) if self._get_column_value_from_row(row, _FIXED_DIVIDEND) else None,
            par_value=int(self._get_column_value_from_row(row, _PAR_VALUE))
        )

    @lru_cache()
    def _get_column_index(self, column_name):
        return _EXPECTED_HEADER_COLUMNS.index(column_name)

    def _get_column_value_from_row(self, row, column_name):
        return row[self._get_column_index(column_name)]

    def get_stock_data(self, stock_name) -> StockExchangeInfo:
        return self._exchange_info_repository[stock_name]

    def get_stock_names(self) -> List[str]:
        return list(self._exchange_info_repository.keys())

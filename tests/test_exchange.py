from super_simple_stocks.exchange import FileExchange

import os

from super_simple_stocks.model import StockExchangeInfo

TEST_FILE = os.path.join(os.path.dirname(__file__), 'test_data.csv')


def test_file_beverage_exchange():
    exchange = FileExchange(TEST_FILE)

    assert exchange.get_stock_data('TEA') == StockExchangeInfo(
        stock_symbol='TEA',
        type='Common',
        last_dividend_per_share=0,
        fixed_dividend_factor=None,
        par_value=100
    )

    assert exchange.get_stock_data('POP') == StockExchangeInfo(
        stock_symbol='POP',
        type='Common',
        last_dividend_per_share=8,
        fixed_dividend_factor=None,
        par_value=100
    )

    assert exchange.get_stock_data('ALE') == StockExchangeInfo(
        stock_symbol='ALE',
        type='Common',
        last_dividend_per_share=23,
        fixed_dividend_factor=None,
        par_value=60
    )

    assert exchange.get_stock_data('GIN') == StockExchangeInfo(
        stock_symbol='GIN',
        type='Preferred',
        last_dividend_per_share=8,
        fixed_dividend_factor=0.02,
        par_value=100
    )

    assert exchange.get_stock_data('JOE') == StockExchangeInfo(
        stock_symbol='JOE',
        type='Common',
        last_dividend_per_share=13,
        fixed_dividend_factor=None,
        par_value=250
    )
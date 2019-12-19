from datetime import datetime, timedelta
from math import sqrt

from super_simple_stocks.model import Trade
from super_simple_stocks.trade_repository import InMemoryTradeRepository

NOW = datetime.now()
TRADES = [
    Trade(
        'test_stock1',
        timestamp=NOW - timedelta(minutes=20),
        quantity=4,
        is_sale=True,
        price=200.0
    ),
    Trade(
        'test_stock1',
        timestamp=NOW - timedelta(minutes=10),
        quantity=1,
        is_sale=True,
        price=100.0
    ),
    Trade(
        'test_stock2',
        timestamp=NOW - timedelta(minutes=10),
        quantity=5,
        is_sale=True,
        price=200.0
    )
]


def test_calculate_stock_price_in_window():
    repository = InMemoryTradeRepository()
    list(map(repository.record_trade, TRADES))

    assert repository.calculate_stock_price_in_window('test_stock1') == 100.0
    assert repository.calculate_stock_price_in_window('test_stock2') == 200.0

    assert repository.calculate_stock_price_in_window('test_stock1', timedelta(minutes=30)) == 180.0
    assert repository.calculate_stock_price_in_window('test_stock2', timedelta(minutes=30)) == 200.0


def test_calculate_gbce_all_share_index_in_window():
    repository = InMemoryTradeRepository()
    list(map(repository.record_trade, TRADES))

    assert abs(
        repository.calculate_gbce_all_share_index_in_window() - sqrt(100.0 * 200.0)
    ) < 1e-10
    assert abs(
        repository.calculate_gbce_all_share_index_in_window(timedelta(minutes=30)) - sqrt(180.0 * 200.0)
    ) < 1e-10

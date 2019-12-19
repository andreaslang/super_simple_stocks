from datetime import datetime, timedelta

from super_simple_stocks.model import Trade
from super_simple_stocks.trade_repository import InMemoryTradeRepository


def test_calculate_stock_price_in_window():
    repository = InMemoryTradeRepository()
    now = datetime.now()
    trades = [
        Trade(
            'test_stock1',
            timestamp=now - timedelta(minutes=20),
            quantity=4,
            is_sale=True,
            price=200.0
        ),
        Trade(
            'test_stock1',
            timestamp=now - timedelta(minutes=10),
            quantity=1,
            is_sale=True,
            price=100.0
        ),
        Trade(
            'test_stock2',
            timestamp=now - timedelta(minutes=10),
            quantity=5,
            is_sale=True,
            price=200.0
        )
    ]

    list(map(repository.record_trade, trades))

    assert repository.calculate_stock_price_in_window('test_stock1') == 100.0
    assert repository.calculate_stock_price_in_window('test_stock2') == 200.0

    assert repository.calculate_stock_price_in_window('test_stock1', timedelta(minutes=30)) == 180.0
    assert repository.calculate_stock_price_in_window('test_stock2', timedelta(minutes=30)) == 200.0

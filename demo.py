import os
from random import Random
from time import sleep

from super_simple_stocks.exchange import Exchange, FileExchange
from super_simple_stocks.model import Trade
from super_simple_stocks.trade_repository import TradeRepository, InMemoryTradeRepository

# This file is just to see everything come together, in reality obviously parts of this would be plugged into a
# stream solution.

# Exchange is a data source which provides stock dividend information and related metrics.
# In the real world this might be a database, here just loaded from a file.
exchange: Exchange = FileExchange(os.path.join(os.path.dirname(__file__), 'tests', 'test_data.csv'))

# Trade repository to record trades against, which also has helper methods to calculate metrics within a trade window
trade_repository: TradeRepository = InMemoryTradeRepository()

# Here I just generate some random trades (not in any sensible way really) and output metrics on every step
stock_names = exchange.get_stock_names()
random = Random()
number_of_trades = 100
for i in range(1, number_of_trades):
    stock_name = random.choice(stock_names)
    trade = Trade(
        stock_symbol=stock_name,
        quantity=random.randint(1, 5),
        price=random.choice([100.0, 1000.0, 5000.0]),
        is_sale=bool(random.randint(0, 1))
    )
    print(f'Recording trade {i}: {trade} ...')
    trade_repository.record_trade(trade)
    stock = exchange.get_stock_data(stock_name)
    price = trade_repository.calculate_stock_price_in_window(stock_name)
    print(f'Updated price {price}')
    print(f'Stock dividend yield {i}: {stock.calculate_dividend_yield(price)}')
    print(f'Stock pe ratio {i}: {stock.calculate_pe_ratio(price)}')
    print(f'GBCE All Share Index: {trade_repository.calculate_gbce_all_share_index_in_window()}')
    print(f'Done Recording trade {i}: {trade}')
    print('')
    sleep(1)


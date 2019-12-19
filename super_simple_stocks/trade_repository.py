import math
from abc import abstractmethod
from datetime import datetime, timedelta
from functools import reduce
from typing import Dict, List

from super_simple_stocks.model import Trade


class TradeRepository:
    """
    Trade repository to record trades and retrieve summary information
    """

    @abstractmethod
    def record_trade(self, trade: Trade):
        pass

    @abstractmethod
    def calculate_stock_price_in_window(self, stock_symbol, window: timedelta = timedelta(minutes=15)):
        pass

    @abstractmethod
    def calculate_gbce_all_share_index_in_window(self, window: timedelta = timedelta(minutes=15)):
        pass


class InMemoryTradeRepository(TradeRepository):

    def __init__(self):
        self._repository: Dict[str, List[Trade]] = {}

    def record_trade(self, trade: Trade):
        if trade.stock_symbol not in self._repository.keys():
            self._repository[trade.stock_symbol] = [trade]
        else:
            self._repository[trade.stock_symbol].append(trade)

    def calculate_stock_price_in_window(self, stock_symbol, window: timedelta = timedelta(minutes=15)) -> float:
        list_of_all_trades = self._repository[stock_symbol]
        fifteen_minutes_ago = datetime.now() - window
        trades_in_time_window = list(filter(lambda trade: trade.timestamp >= fifteen_minutes_ago, list_of_all_trades))
        total_amount = sum(map(lambda trade: trade.price * trade.quantity, trades_in_time_window))
        total_quantity = sum(map(lambda trade: trade.quantity, trades_in_time_window))
        return total_amount / total_quantity

    def calculate_gbce_all_share_index_in_window(self, window: timedelta = timedelta(minutes=15)):
        # Calculating a product this large will almost certainly fail for any real example
        # therefore we first move the nth root product of prices into (natural) log space, which means it is
        # a sum of the logs divided by n and then we bring it back into normal space by using e^result.
        price_product_in_log_space = reduce(
            lambda agg_stock_price, stock_symbol: agg_stock_price + math.log(self.calculate_stock_price_in_window(
                stock_symbol, window
            )),
            self._repository.keys(),
            0.0
        )
        return math.e**(price_product_in_log_space / len(self._repository))


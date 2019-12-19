from abc import abstractmethod
from datetime import datetime, timedelta
from typing import Dict, List

from super_simple_stocks.model import Trade


class TradeRepository:

    @abstractmethod
    def record_trade(self, trade: Trade):
        pass

    @abstractmethod
    def calculate_stock_price_in_window(self, stock_symbol, window: timedelta = timedelta(minutes=15)):
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
        print(list(trades_in_time_window))
        total_amount = sum(map(lambda trade: trade.price * trade.quantity, trades_in_time_window))
        total_quantity = sum(map(lambda trade: trade.quantity, trades_in_time_window))
        return total_amount / total_quantity


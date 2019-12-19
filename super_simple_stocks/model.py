from typing import NamedTuple, Optional


class StockExchangeInfo(NamedTuple):
    stock_symbol: str
    type: str
    last_dividend_per_share: Optional[int]
    par_value: int
    fixed_dividend_factor: Optional[float] = None

from functools import lru_cache
from typing import NamedTuple, Optional


class StockExchangeInfo(NamedTuple):
    stock_symbol: str
    type: str
    last_dividend_per_share: Optional[int]
    par_value: int
    fixed_dividend_factor: Optional[float] = None

    @lru_cache()
    def calculate_dividend(self) -> float:
        if 'Common' == self.type:
            return float(self.last_dividend_per_share)
        elif 'Preferred' == self.type:
            return self.fixed_dividend_factor * self.par_value
        else:
            raise NotImplementedError(
                f'There is no implementation to calculate dividend yield for stock type: "{self.type}".'
            )

    def calculate_dividend_yield(self, ticker_price: float) -> Optional[float]:
        return self.calculate_dividend() / ticker_price if ticker_price != 0.0 else None

    def calculate_pe_ratio(self, ticker_price: float) -> Optional[float]:
        dividend = self.calculate_dividend()
        return ticker_price / dividend if dividend != 0.0 else None

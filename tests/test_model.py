from super_simple_stocks.model import StockExchangeInfo

_common_zero_last_dividend = StockExchangeInfo(
    stock_symbol='foo',
    type='Common',
    last_dividend_per_share=0,
    fixed_dividend_factor=None,
    par_value=100
)

_common_non_zero_last_dividend = StockExchangeInfo(
    stock_symbol='foo',
    type='Common',
    last_dividend_per_share=20,
    fixed_dividend_factor=None,
    par_value=100
)

_preferred_zero_last_dividend = StockExchangeInfo(
    stock_symbol='bar',
    type='Preferred',
    last_dividend_per_share=0,
    fixed_dividend_factor=0.02,
    par_value=100
)


def test_calculate_dividend():
    assert _common_zero_last_dividend.calculate_dividend() == 0.0
    assert _common_non_zero_last_dividend.calculate_dividend() == 20.0
    assert _preferred_zero_last_dividend.calculate_dividend() == 2.0


def test_calculate_dividend_yield():
    assert _common_zero_last_dividend.calculate_dividend_yield(10.0) == 0.0
    assert _common_non_zero_last_dividend.calculate_dividend_yield(10.0) == 2.0
    assert _preferred_zero_last_dividend.calculate_dividend_yield(10.0) == 0.2

    assert _preferred_zero_last_dividend.calculate_dividend_yield(0.0) is None


def test_calculate_pe_ratio():
    assert _common_non_zero_last_dividend.calculate_pe_ratio(10.0) == 0.5
    assert _preferred_zero_last_dividend.calculate_pe_ratio(10.0) == 5.0

    assert _common_zero_last_dividend.calculate_pe_ratio(10.0) is None

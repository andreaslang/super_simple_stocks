
def convert_percentage_string_to_factor(raw_value: str):
    try:
        return int(raw_value.replace('%', '')) / 100.0
    except Exception as e:
        raise RuntimeError(f'Cannot convert {raw_value} to factor.') from e

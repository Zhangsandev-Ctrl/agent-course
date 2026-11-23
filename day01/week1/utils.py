def is_valid_money(value):
    """判断金额是否为合法正数(排除 bool)。"""
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0

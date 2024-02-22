def get_currency_format(data) -> str:
    if not data:
        return "$"
    return "$ {:,.2f}".format(data)
def get_dividend_sum_for_symbol(book: Book, symbol: str):
    svc = SecuritiesAggregate(book)
    security = svc.get_by_symbol(symbol)
    sec_svc = SecurityAggregate(book, security)
    accounts = sec_svc.get_income_accounts()
    total = Decimal(0)
    for account in accounts:
        income = get_dividend_sum(book, account)
        total += income
    return total
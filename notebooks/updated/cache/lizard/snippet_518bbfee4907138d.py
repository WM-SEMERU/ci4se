def __store_cash_balances_per_currency(self, cash_balances):
    cash = self.model.get_cash_asset_class()
    for cur_symbol in cash_balances:
        item = CashBalance(cur_symbol)
        item.parent = cash
        quantity = cash_balances[cur_symbol]['total']
        item.value = Decimal(quantity)
        item.currency = cur_symbol
        cash.stocks.append(item)
        self.model.stocks.append(item)
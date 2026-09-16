def market_if_touched_replace(self, accountID, orderID, **kwargs):
    return self.replace(accountID, orderID, order=
        MarketIfTouchedOrderRequest(**kwargs))
def find_unallocated_holdings(self):
    session = self.open_session()
    linked_entities = session.query(AssetClassStock).all()
    linked = []
    for item in linked_entities:
        linked.append(item.symbol)
    from .stocks import StocksInfo
    stocks = StocksInfo()
    stocks.logger = self.logger
    holdings = stocks.get_symbols_with_positive_balances()
    non_alloc = []
    index = -1
    for item in holdings:
        try:
            index = linked.index(item)
            self.logger.debug(index)
        except ValueError:
            non_alloc.append(item)
    return non_alloc
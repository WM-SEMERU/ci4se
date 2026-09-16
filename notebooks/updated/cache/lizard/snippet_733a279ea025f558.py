def tickerId(self, contract_identifier):
    symbol = contract_identifier
    if isinstance(symbol, Contract):
        symbol = self.contractString(symbol)
    for tickerId in self.tickerIds:
        if symbol == self.tickerIds[tickerId]:
            return tickerId
    else:
        tickerId = len(self.tickerIds)
        self.tickerIds[tickerId] = symbol
        return tickerId
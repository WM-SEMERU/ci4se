def prices(self):
    if not self.__prices_aggregate:
        self.__prices_aggregate = PricesAggregate(self.book)
    return self.__prices_aggregate
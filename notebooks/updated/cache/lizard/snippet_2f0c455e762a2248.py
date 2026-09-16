def book(self, name):
    self._validate_order_book(name)
    return OrderBook(name, self._rest_client, self._logger)
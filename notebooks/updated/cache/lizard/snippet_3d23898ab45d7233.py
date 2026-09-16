def process_orders(self, orderbook):
    for stock, alloc in orderbook.iteritems():
        self.logger.info('{}: Ordered {} {} stocks'.format(self.datetime,
            stock, alloc))
        if isinstance(alloc, int):
            self.order(stock, alloc)
        elif isinstance(alloc, float) and alloc >= -1 and alloc <= 1:
            self.order_percent(stock, alloc)
        else:
            self.logger.warning('{}: invalid order for {}: {})'.format(self
                .datetime, stock, alloc))
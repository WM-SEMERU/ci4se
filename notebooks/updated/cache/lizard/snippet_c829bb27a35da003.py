def get_all_orders_ungrouped(self):
    for olist in self._orders.values():
        for order in olist.orders:
            yield order
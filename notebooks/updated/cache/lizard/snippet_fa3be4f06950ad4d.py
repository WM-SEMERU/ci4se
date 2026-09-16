def order_by(self, column, direction='asc'):
    if self.unions:
        prop = 'union_orders'
    else:
        prop = 'orders'
    if direction.lower() == 'asc':
        direction = 'asc'
    else:
        direction = 'desc'
    getattr(self, prop).append({'column': column, 'direction': direction})
    return self
def tail(self, limit=25, **fetch_kwargs):
    return self.fetch(order_by='KEY DESC', limit=limit, **fetch_kwargs)[::-1]
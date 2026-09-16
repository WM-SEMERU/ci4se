def transactions(self, cursor=None, order='asc', limit=10, sse=False):
    return self.horizon.account_transactions(self.address, cursor=cursor,
        order=order, limit=limit, sse=sse)
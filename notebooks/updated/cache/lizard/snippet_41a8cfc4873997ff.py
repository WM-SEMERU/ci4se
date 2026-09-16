def trans_history(self, from_=None, count=None, from_id=None, end_id=None,
    order=None, since=None, end=None):
    return self._trade_api_call('TransHistory', from_=from_, count=count,
        from_id=from_id, end_id=end_id, order=order, since=since, end=end)
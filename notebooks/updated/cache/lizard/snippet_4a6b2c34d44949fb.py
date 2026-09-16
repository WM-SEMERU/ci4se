def read(self, symbol, as_of=None):
    if as_of is not None:
        res = self.find_one({'symbol': symbol, 'start_time': {'$lte': as_of
            }}, sort=[('start_time', pymongo.DESCENDING)])
    else:
        res = self.find_one({'symbol': symbol}, sort=[('start_time',
            pymongo.DESCENDING)])
    return res['metadata'] if res is not None else None
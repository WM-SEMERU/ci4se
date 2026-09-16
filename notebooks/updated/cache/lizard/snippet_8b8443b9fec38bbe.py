def sum(self, callback=None):
    if callback is None:
        return sum(self.items)
    callback = self._value_retriever(callback)
    return self.reduce(lambda result, item: (result or 0) + callback(item))
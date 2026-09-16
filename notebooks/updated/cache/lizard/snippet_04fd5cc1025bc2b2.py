def query(self, model_cls):
    self._filters_cmd = list()
    self.query_filters = list()
    self._order_by_cmd = None
    self._offset = 0
    self._limit = 0
    self.query_class = model_cls._name
    return self
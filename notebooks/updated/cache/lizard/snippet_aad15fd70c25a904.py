def set_filters(self, filters):
    if filters == None or isinstance(filters, (tuple, list)):
        self.filters = filters
    else:
        self.filters = [filters]
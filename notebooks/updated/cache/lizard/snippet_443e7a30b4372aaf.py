def add_filter_function(self, name, new_function):
    self._filter_functions[name] = new_function
    self.invalidateFilter()
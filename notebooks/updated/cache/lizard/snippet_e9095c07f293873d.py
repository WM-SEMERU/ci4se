def define_example_values(self, http_method, route, values, update=False):
    self.defined_example_values[http_method.lower(), route] = {'update':
        update, 'values': values}
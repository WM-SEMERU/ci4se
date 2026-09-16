def _create_node(self, name, parent, children, data):
    self._db[name] = {'parent': parent, 'children': children, 'data': data}
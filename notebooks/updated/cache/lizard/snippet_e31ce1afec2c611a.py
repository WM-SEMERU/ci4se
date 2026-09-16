def get_by_name(self, name):
    result = self.get_by('name', name)
    if result:
        data = result[0]
        new_resource = self.new(self._connection, data)
    else:
        new_resource = None
    return new_resource
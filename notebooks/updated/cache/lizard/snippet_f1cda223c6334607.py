def build_resource(self, data):
    if self._res_class is None:
        self._res_class = self._details.session.get_resource(self._details.
            service_name, self._details.resource)
    final_data = {}
    for key, value in data.items():
        final_data[to_snake_case(key)] = value
    return self._res_class(connection=self._connection, **final_data)
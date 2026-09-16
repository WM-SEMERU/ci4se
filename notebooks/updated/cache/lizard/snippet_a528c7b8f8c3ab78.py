def raw_query(self, query, format=None, pretty=False):
    if format:
        format = format
    else:
        format = self.format
    payload = self._payload_builder(query, format=format)
    response = self.execute_query(payload)
    if pretty:
        response = self.response_builder(response)
    return response
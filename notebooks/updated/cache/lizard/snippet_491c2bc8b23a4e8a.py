def response_helper(self, response, **kwargs):
    self.resolve_schema(response)
    if 'headers' in response:
        for header in response['headers'].values():
            self.resolve_schema(header)
    return response
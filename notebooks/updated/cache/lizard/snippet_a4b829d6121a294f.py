def set_field_value(self, field_name, value):
    if self.response is None:
        return
    if 'data' in self.response:
        items = self.response['data']
    else:
        items = [self.response]
    for item in items:
        item[field_name] = value
def json_data(self, instance, default=None):
    value = self.get(instance)
    if value and self.is_multi_valued():
        return map(api.get_url_info, value)
    elif value and not self.is_multi_valued():
        return api.get_url_info(value)
    return value or default
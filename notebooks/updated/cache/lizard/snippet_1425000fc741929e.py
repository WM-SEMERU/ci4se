def js_output(self, attrs=None):
    result = []
    items = sorted(self.items())
    for key, value in items:
        result.append(value.js_output(attrs))
    return _nulljoin(result)
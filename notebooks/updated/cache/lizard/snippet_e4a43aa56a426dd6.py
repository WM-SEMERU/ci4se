def timeout(self):
    value = self._body.get('timeout', '0s')
    value = value[:-1]
    return float(value)
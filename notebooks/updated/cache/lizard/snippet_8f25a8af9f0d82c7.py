def get_absolute_limits(self):
    resp, body = self.method_get('/limits')
    absolute_limits = body.get('limits', {}).get('absolute')
    return absolute_limits
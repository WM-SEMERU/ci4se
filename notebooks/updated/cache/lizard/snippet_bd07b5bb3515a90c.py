def is_valid_api_key(self):
    res = self.send('api/v3/api_keys', 'get')
    return res.ok and self.api_key in (ak['token'] for ak in res.json()[
        'result'])
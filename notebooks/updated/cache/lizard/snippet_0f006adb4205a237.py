def remove_kv_store(self, key):
    data = {'operation': 'DELETE', 'key': key}
    return self.post(self.make_url('/useragent-kv'), data=to_json(data),
        headers=self.default_headers).text
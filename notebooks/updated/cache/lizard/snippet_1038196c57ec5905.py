def expire_at(self, key, _time):
    return self._client.expireat(self.get_key(key), round(_time))
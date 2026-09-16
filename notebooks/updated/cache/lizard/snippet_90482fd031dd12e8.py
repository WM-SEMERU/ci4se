def list_buckets(self, offset=0, limit=100):
    if limit > 100:
        raise Exception("Zenobase can't handle limits over 100")
    return self._get('/users/{}/buckets/?order=label&offset={}&limit={}'.
        format(self.client_id, offset, limit))
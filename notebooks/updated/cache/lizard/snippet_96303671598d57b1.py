def get_raw_data(self, url, *args, **kwargs):
    res = self._conn.get(url, headers=self._prepare_headers(**kwargs))
    if res.status_code == 200:
        return res.content
    else:
        return None
def get_data(self, url, *args, **kwargs):
    res = self._conn.get(url, headers=self._prepare_headers(**kwargs))
    if res.status_code == 200:
        return res.text
    else:
        return None
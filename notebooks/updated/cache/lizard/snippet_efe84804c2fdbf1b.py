def delete_multireddit(self, name, *args, **kwargs):
    url = self.config['multireddit_about'].format(user=self.user.name,
        multi=name)
    if not self._use_oauth:
        self.http.headers['x-modhash'] = self.modhash
    try:
        self.request(url, *args, data={}, method='DELETE', **kwargs)
    finally:
        if not self._use_oauth:
            del self.http.headers['x-modhash']
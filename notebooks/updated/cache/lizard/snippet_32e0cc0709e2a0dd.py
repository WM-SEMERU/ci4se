def get_notables(self, id_num):
    url = self._build_url('my', 'activities', id_num, 'notables')
    return self._json(url)
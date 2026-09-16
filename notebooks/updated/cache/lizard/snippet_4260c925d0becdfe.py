def get_subjects(self):
    res = requests.get(self._url('/subjects'))
    raise_if_failed(res)
    return res.json()
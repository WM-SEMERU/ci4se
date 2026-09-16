def create_activity(self, data):
    url = self._build_url('my', 'activities')
    if isinstance(data, dict):
        data = json.dumps(data)
    r = self.session.post(url, data=data)
    r.raise_for_status()
    return r
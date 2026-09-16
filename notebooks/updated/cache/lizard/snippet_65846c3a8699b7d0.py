def entityId(self, partial, channel=None):
    url = '{}/{}/meta/any'.format(self.url, _get_path(partial))
    data = self._get(_add_channel(url, channel))
    return data.json()['Id']
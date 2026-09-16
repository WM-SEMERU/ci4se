def moz_info(self):
    if 'moz_info' not in self._memo:
        self._memo['moz_info'] = _get_url(self.artifact_url('mozinfo.json')
            ).json()
    return self._memo['moz_info']
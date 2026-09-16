def set_playback(self, playback):
    req_url = ENDPOINTS['setPlayback'].format(self._ip_address)
    params = {'playback': playback}
    return request(req_url, params=params)
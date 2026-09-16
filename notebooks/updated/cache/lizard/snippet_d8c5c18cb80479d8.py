def check_new_videos(self):
    resp = api.request_videos(self.blink, time=self.blink.last_refresh, page=0)
    for camera in self.cameras.keys():
        self.motion[camera] = False
    try:
        info = resp['videos']
    except (KeyError, TypeError):
        _LOGGER.warning('Could not check for motion. Response: %s', resp)
        return False
    for entry in info:
        try:
            name = entry['camera_name']
            clip = entry['address']
            timestamp = entry['created_at']
            self.motion[name] = True
            self.last_record[name] = {'clip': clip, 'time': timestamp}
        except KeyError:
            _LOGGER.debug('No new videos since last refresh.')
    return True
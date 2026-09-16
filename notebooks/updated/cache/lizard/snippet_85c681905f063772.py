def get_current_notification(self):
    log.debug('getting visible notification...')
    cmd, url = DEVICE_URLS['get_current_notification']
    return self._exec(cmd, url)
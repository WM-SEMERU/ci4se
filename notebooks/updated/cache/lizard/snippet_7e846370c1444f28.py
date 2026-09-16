def state(self):
    if self.method in ['OPTIONS', 'DESCRIBE', 'SETUP', 'PLAY']:
        state = STATE_STARTING
    elif self.method in ['KEEP-ALIVE']:
        state = STATE_PLAYING
    else:
        state = STATE_STOPPED
    _LOGGER.debug('RTSP session (%s) state %s', self.host, state)
    return state
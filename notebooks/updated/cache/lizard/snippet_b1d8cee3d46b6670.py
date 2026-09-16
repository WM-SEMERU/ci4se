def _play(self):
    if self._input_func in self._netaudio_func_list:
        body = {'cmd0': 'PutNetAudioCommand/CurEnter', 'cmd1':
            'aspMainZone_WebUpdateStatus/', 'ZoneName': 'MAIN ZONE'}
        try:
            if self.send_post_command(self._urls.command_netaudio_post, body):
                self._state = STATE_PLAYING
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            _LOGGER.error('Connection error: play command not sent.')
            return False
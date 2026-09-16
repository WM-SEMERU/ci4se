def previous_track(self):
    if self._input_func in self._netaudio_func_list:
        body = {'cmd0': 'PutNetAudioCommand/CurUp', 'cmd1':
            'aspMainZone_WebUpdateStatus/', 'ZoneName': 'MAIN ZONE'}
        try:
            return bool(self.send_post_command(self._urls.
                command_netaudio_post, body))
        except requests.exceptions.RequestException:
            _LOGGER.error('Connection error: previous track command not sent.')
            return False
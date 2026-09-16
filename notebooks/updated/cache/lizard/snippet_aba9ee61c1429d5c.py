def mpris(self):
    if self._kill:
        raise KeyboardInterrupt
    current_player_id = self._player_details.get('id')
    cached_until = self.py3.CACHE_FOREVER
    if self._player is None:
        text = self.format_none
        color = self.py3.COLOR_BAD
        composite = [{'full_text': text, 'color': color}]
        self._data = {}
    else:
        self._init_data()
        text, color, cached_until = self._get_text()
        self._control_states = self._get_control_states()
        buttons = self._get_response_buttons()
        composite = self.py3.safe_format(self.format, dict(text, **buttons))
    if self._data.get('error_occurred'
        ) or current_player_id != self._player_details.get('id'):
        self._tries += 1
        if self._tries < 3:
            return self.mpris()
        composite = [{'full_text': 'Something went wrong', 'color': self.
            py3.COLOR_BAD}]
        cached_until = self.py3.time_in(1)
    response = {'cached_until': cached_until, 'color': color, 'composite':
        composite}
    self._tries = 0
    return response
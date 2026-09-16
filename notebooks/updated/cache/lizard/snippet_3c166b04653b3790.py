def set_is_playable(self, is_playable):
    value = 'false'
    if is_playable:
        value = 'true'
    self.set_property('isPlayable', value)
    self.is_folder = not is_playable
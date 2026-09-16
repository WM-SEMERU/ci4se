def parse_channels(self):
    channels = []
    for channel in self._project_dict['channels']:
        channels.append(Channel(channel, self._is_sixteen_bit, self.
            _ignore_list))
    return channels
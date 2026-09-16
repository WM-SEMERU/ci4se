def part_channel(self, channel, reason=None, tags=None):
    params = [channel]
    if reason:
        params.append(reason)
    self.send('PART', params=params, tags=tags)
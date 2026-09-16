def get_channel_access_token(self, channel):
    if isinstance(channel, models.Channel):
        channel = channel.name
    r = self.oldapi_request('GET', 'channels/%s/access_token' % channel).json()
    return r['token'], r['sig']
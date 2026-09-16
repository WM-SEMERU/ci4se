def geo(self):
    if isinstance(self.media, (types.MessageMediaGeo, types.
        MessageMediaGeoLive, types.MessageMediaVenue)):
        return self.media.geo
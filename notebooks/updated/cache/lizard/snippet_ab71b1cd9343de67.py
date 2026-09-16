def auto_track_url(track):
    hub = track.root(cls=Hub)
    if hub is None:
        raise ValueError(
            'track is not fully connected because the root is %s' % repr(hub))
    if hub.url is None:
        raise ValueError('hub.url is not set')
    if track.source is None:
        raise ValueError('track.source is not set')
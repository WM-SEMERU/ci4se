def get_track_scrobbles(self, artist, track, cacheable=False):
    params = self._get_params()
    params['artist'] = artist
    params['track'] = track
    seq = []
    for track in _collect_nodes(None, self, self.ws_prefix +
        '.getTrackScrobbles', cacheable, params):
        title = _extract(track, 'name')
        artist = _extract(track, 'artist')
        date = _extract(track, 'date')
        album = _extract(track, 'album')
        timestamp = track.getElementsByTagName('date')[0].getAttribute('uts')
        seq.append(PlayedTrack(Track(artist, title, self.network), album,
            date, timestamp))
    return seq
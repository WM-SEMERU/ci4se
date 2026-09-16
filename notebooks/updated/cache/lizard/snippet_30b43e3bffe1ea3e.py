def total_time(self):
    now_playing = self._setstate.nowPlayingInfo
    if now_playing.HasField('duration'):
        return int(now_playing.duration)
    return None
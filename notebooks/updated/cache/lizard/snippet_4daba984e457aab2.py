def _seek_streamer(self, index, value):
    highest_id = self._rsl.highest_stored_id()
    streamer = self.graph.streamers[index]
    if not streamer.walker.buffered:
        return _pack_sgerror(SensorLogError.CANNOT_USE_UNBUFFERED_STREAM)
    find_type = None
    try:
        exact = streamer.walker.seek(value, target='id')
        if exact:
            find_type = 'exact'
        else:
            find_type = 'other_stream'
    except UnresolvedIdentifierError:
        if value > highest_id:
            find_type = 'too_high'
        else:
            find_type = 'too_low'
    if find_type == 'exact':
        try:
            streamer.walker.pop()
        except StreamEmptyError:
            pass
        error = Error.NO_ERROR
    elif find_type == 'too_high':
        streamer.walker.skip_all()
        error = _pack_sgerror(SensorLogError.NO_MORE_READINGS)
    elif find_type == 'too_low':
        streamer.walker.seek(0, target='offset')
        error = _pack_sgerror(SensorLogError.NO_MORE_READINGS)
    else:
        error = _pack_sgerror(SensorLogError.ID_FOUND_FOR_ANOTHER_STREAM)
    return error
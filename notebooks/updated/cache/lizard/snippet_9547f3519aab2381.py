def _retrieve(self, namespace, stream, start_id, end_time, order, limit,
    configuration):
    start_id_event = Event(start_id)
    end_id_event = Event(uuid_from_kronos_time(end_time, _type=UUIDType.
        HIGHEST))
    stream_events = self.db[namespace][stream]
    lo = bisect.bisect_left(stream_events, start_id_event)
    if lo + 1 > len(stream_events):
        return
    if stream_events[lo] == start_id_event:
        lo += 1
    hi = bisect.bisect_right(stream_events, end_id_event)
    if order == ResultOrder.DESCENDING:
        index_it = xrange(hi - 1, lo - 1, -1)
    else:
        index_it = xrange(lo, hi)
    for i in index_it:
        if limit <= 0:
            break
        limit -= 1
        yield marshal.dumps(stream_events[i])
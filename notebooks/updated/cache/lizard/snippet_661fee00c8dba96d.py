def barrier(events, sid, kind='neighbour'):
    events[sid].set()
    if kind == 'neighbour':
        if sid > 0:
            logging.debug('{0} is waiting for {1}'.format(sid, sid - 1))
            events[sid - 1].wait()
        if sid < len(bkg_events) - 1:
            logging.debug('{0} is waiting for {1}'.format(sid, sid + 1))
            events[sid + 1].wait()
    else:
        [e.wait() for e in events]
    return
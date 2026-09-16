def thread_data(name, value=NOTHING, ct=None):
    ct = ct or current_thread()
    if is_mainthread(ct):
        loc = process_data()
    elif not hasattr(ct, '_pulsar_local'):
        ct._pulsar_local = loc = {}
    else:
        loc = ct._pulsar_local
    if value is not NOTHING:
        if name in loc:
            if loc[name] is not value:
                raise RuntimeError('%s is already available on this thread' %
                    name)
        else:
            loc[name] = value
    return loc.get(name)
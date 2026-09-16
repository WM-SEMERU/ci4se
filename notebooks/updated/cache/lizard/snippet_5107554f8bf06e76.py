def host_trigger(trg_queue, user=None, group=None, mode=None):
    trigger(trg_queue, user=user, group=group, mode=mode, trigger=_c.
        FSQ_HOSTS_TRIGGER)
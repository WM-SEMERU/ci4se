def get_global_tor(reactor, control_port=None, progress_updates=None,
    _tor_launcher=None):
    tor = yield get_global_tor_instance(reactor, control_port=control_port,
        progress_updates=progress_updates, _tor_launcher=_tor_launcher)
    cfg = yield tor.get_config()
    defer.returnValue(cfg)
def init(path=None):
    default = get_default()
    if default is not None and not isinstance(default, VoidLogKeeper):
        return default
    tee = LogTee()
    set_default(tee)
    FluLogKeeper.init(path)
    tee.add_keeper('flulog', FluLogKeeper())
    return tee
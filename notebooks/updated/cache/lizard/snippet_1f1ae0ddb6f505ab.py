def from_protocol(proto):
    cfg = TorConfig(control=proto)
    yield cfg.post_bootstrap
    defer.returnValue(cfg)
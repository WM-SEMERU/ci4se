def publish(tgt, fun, arg=None, tgt_type='glob', returner='', timeout=5,
    roster=None):
    return _publish(tgt, fun, arg=arg, tgt_type=tgt_type, returner=returner,
        timeout=timeout, form='clean', roster=roster)
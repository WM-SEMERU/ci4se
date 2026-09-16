def _make_futures(futmap_keys, class_check, make_result_fn):
    futmap = {}
    for key in futmap_keys:
        if class_check is not None and not isinstance(key, class_check):
            raise ValueError('Expected list of {}'.format(type(class_check)))
        futmap[key] = concurrent.futures.Future()
        if not futmap[key].set_running_or_notify_cancel():
            raise RuntimeError('Future was cancelled prematurely')
    f = concurrent.futures.Future()
    f.add_done_callback(lambda f: make_result_fn(f, futmap))
    if not f.set_running_or_notify_cancel():
        raise RuntimeError('Future was cancelled prematurely')
    return f, futmap
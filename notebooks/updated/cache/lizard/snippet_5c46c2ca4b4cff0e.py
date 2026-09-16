def returner(ret):
    opts = _get_options(ret)
    metric_base = ret['fun']
    if not metric_base.startswith('virt.'):
        metric_base += '.' + ret['id'].replace('.', '_')
    saltdata = ret['return']
    _send(saltdata, metric_base, opts)
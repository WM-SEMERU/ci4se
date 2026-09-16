def status(name, sig=None):
    proxy_fn = 'dummy.service_status'
    resp = __proxy__[proxy_fn](name)
    if resp['comment'] == 'stopped':
        return False
    if resp['comment'] == 'running':
        return True
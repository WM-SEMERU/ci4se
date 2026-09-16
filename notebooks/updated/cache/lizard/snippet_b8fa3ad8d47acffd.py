def migrate_keys(self, host, port, keys, dest_db, timeout, *, copy=False,
    replace=False):
    if not isinstance(host, str):
        raise TypeError('host argument must be str')
    if not isinstance(timeout, int):
        raise TypeError('timeout argument must be int')
    if not isinstance(dest_db, int):
        raise TypeError('dest_db argument must be int')
    if not isinstance(keys, (list, tuple)):
        raise TypeError('keys argument must be list or tuple')
    if not host:
        raise ValueError('Got empty host')
    if dest_db < 0:
        raise ValueError('dest_db must be greater equal 0')
    if timeout < 0:
        raise ValueError('timeout must be greater equal 0')
    if not keys:
        raise ValueError('keys must not be empty')
    flags = []
    if copy:
        flags.append(b'COPY')
    if replace:
        flags.append(b'REPLACE')
    flags.append(b'KEYS')
    flags.extend(keys)
    fut = self.execute(b'MIGRATE', host, port, '', dest_db, timeout, *flags)
    return wait_ok(fut)
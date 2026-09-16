def select(self, db):
    if not isinstance(db, int):
        raise TypeError('DB must be of int type, not {!r}'.format(db))
    if db < 0:
        raise ValueError('DB must be greater or equal 0, got {!r}'.format(db))
    fut = self.execute('SELECT', db)
    return wait_ok(fut)
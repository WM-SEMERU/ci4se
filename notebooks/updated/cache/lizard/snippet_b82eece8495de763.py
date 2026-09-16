def direct_call(self, *args):
    conn = redis.Redis(connection_pool=self.pool)
    command = args[0]
    key = self._namespace(args[1])
    args = args[2:]
    func = getattr(conn, command)
    return func(key, *args)
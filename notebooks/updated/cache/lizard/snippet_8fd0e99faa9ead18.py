def execute(self, query, args=None):
    conn = self._get_db()
    while (yield self.nextset()):
        pass
    if PY2:
        encoding = conn.encoding

        def ensure_bytes(x):
            if isinstance(x, unicode):
                x = x.encode(encoding)
            return x
        query = ensure_bytes(query)
        if args is not None:
            if isinstance(args, (tuple, list)):
                args = tuple(map(ensure_bytes, args))
            elif isinstance(args, dict):
                args = dict((ensure_bytes(key), ensure_bytes(val)) for key,
                    val in args.items())
            else:
                args = ensure_bytes(args)
    if args is not None:
        query = query % self._escape_args(args, conn)
    yield self._query(query)
    self._executed = query
    raise gen.Return(self.rowcount)
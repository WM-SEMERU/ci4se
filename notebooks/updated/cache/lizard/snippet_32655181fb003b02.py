def callproc(self, procname, args=()):
    conn = self._get_db()
    if args:
        fmt = '@_{0}_%d=%s'.format(procname)
        self._query('SET %s' % ','.join(fmt % (index, conn.escape(arg)) for
            index, arg in enumerate(args)))
        self.nextset()
    q = 'CALL %s(%s)' % (procname, ','.join([('@_%s_%d' % (procname, i)) for
        i in range_type(len(args))]))
    self._query(q)
    self._executed = q
    return args
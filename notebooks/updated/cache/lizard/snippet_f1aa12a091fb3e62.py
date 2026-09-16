def execute(self, sql, args=None):
    con = self.pool.pop()
    c = None
    try:
        c = con.cursor()
        LOGGER.debug('Execute sql: ' + sql + ' args:' + str(args))
        if type(args) is tuple:
            c.execute(sql, args)
        elif type(args) is list:
            if len(args) > 1 and type(args[0]) in (list, tuple):
                c.executemany(sql, args)
            else:
                c.execute(sql, args)
        elif args is None:
            c.execute(sql)
        if sql.lstrip()[:6].upper() == 'INSERT':
            return c.lastrowid
        return c.rowcount
    except Exception as e:
        LOGGER.error('Error Execute on %s', str(e))
        raise DBError(str(e))
    finally:
        c and c.close()
        con and self.pool.push(con)
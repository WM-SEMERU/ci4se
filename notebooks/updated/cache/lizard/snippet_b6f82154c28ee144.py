def execute_catch(c, sql, vars=None):
    try:
        c.execute(sql, vars)
    except Exception as err:
        cmd = sql.split(' ', 1)[0]
        log.error('Error executing %s: %s', cmd, err)
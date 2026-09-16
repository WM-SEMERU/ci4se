def _get_cursor(self):
    _options = self._get_options()
    conn = psycopg2.connect(host=_options['host'], user=_options['user'],
        password=_options['pass'], dbname=_options['db'], port=_options['port']
        )
    cursor = conn.cursor()
    try:
        yield cursor
        log.debug('Connected to POSTGRES DB')
    except psycopg2.DatabaseError as err:
        log.exception('Error in ext_pillar POSTGRES: %s', err.args)
    finally:
        conn.close()
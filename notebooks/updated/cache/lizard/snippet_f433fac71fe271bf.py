def readquery(sqlQuery, dbConn, log, quiet=False):
    log.debug('starting the ``readquery`` function')
    import pymysql
    import warnings
    warnings.filterwarnings('error', category=pymysql.Warning)
    rows = []
    try:
        cursor = dbConn.cursor(pymysql.cursors.DictCursor)
    except Exception as e:
        log.error('could not create the database cursor: %s' % (e,))
        raise IOError('could not create the database cursor: %s' % (e,))
    cursor.execute(sqlQuery)
    rows = cursor.fetchall()
    try:
        cursor.execute(sqlQuery)
        rows = cursor.fetchall()
    except Exception as e:
        sqlQuery = sqlQuery[:1000]
        if quiet == False:
            log.warning(
                'MySQL raised an error - read command not executed.\n' +
                str(e) + """
Here is the sqlQuery
	%(sqlQuery)s""" % locals())
            raise e
    try:
        cursor.close()
    except Exception as e:
        log.warning('could not close the db cursor ' + str(e) + '\n')
    log.debug('completed the ``readquery`` function')
    return rows
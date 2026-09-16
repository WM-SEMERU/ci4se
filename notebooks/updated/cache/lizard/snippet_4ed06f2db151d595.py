def database_caller_creator(self, host, port, password, username, name=None):
    cursor = None
    conn = None
    try:
        if name:
            db = name
        else:
            db = 'mysql_' + str_generator(self)
        conn = mysql.connector.connect(user=username, host=host, port=port,
            password=password)
        cursor = conn.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS ' + db +
            ' DEFAULT CHARACTER SET utf8')
        cursor.execute('USE ' + db)
        logger.warning('Database created and opened succesfully: %s' % db,
            extra=extra_information)
    except mysql.connector.Error as err:
        logger.error(err.msg, extra=extra_information)
        sys.exit(1)
    return cursor, conn
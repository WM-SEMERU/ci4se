def create_mysql_db(db_url):
    db_url = db_url.strip().strip('/')
    if db_url.find('mysql') >= 0:
        db_name = config.get('mysqld', 'db_name', 'hydradb')
        if db_url.find(db_name) >= 0:
            no_db_url = db_url.rsplit('/', 1)[0]
        else:
            if db_url.find('@') == -1:
                raise HydraError('No Hostname specified in DB url')
            host_and_db_name = db_url.split('@')[1]
            if host_and_db_name.find('/') >= 0:
                no_db_url, db_name = db_url.rsplit('/', 1)
            else:
                no_db_url = db_url
                db_url = no_db_url + '/' + db_name
        db_url = '{}?charset=utf8&use_unicode=1'.format(db_url)
        if config.get('mysqld', 'auto_create', 'Y') == 'Y':
            tmp_engine = create_engine(no_db_url)
            log.warning('Creating database {0} as it does not exist.'.
                format(db_name))
            tmp_engine.execute('CREATE DATABASE IF NOT EXISTS {0}'.format(
                db_name))
    return db_url
def dump(state, host, remote_filename, database=None, mysql_user=None,
    mysql_password=None, mysql_host=None, mysql_port=None):
    yield '{0} > {1}'.format(make_mysql_command(executable='mysqldump',
        database=database, user=mysql_user, password=mysql_password, host=
        mysql_host, port=mysql_port), remote_filename)
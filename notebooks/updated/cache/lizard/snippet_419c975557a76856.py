def get_default_config_help(self):
    config_help = super(PostgresqlCollector, self).get_default_config_help()
    config_help.update({'host': 'Hostname', 'dbname':
        'DB to connect to in order to get list of DBs in PgSQL', 'user':
        'Username', 'password': 'Password', 'port': 'Port number',
        'password_provider':
        'Whether to auth with supplied password or .pgpass file  <password|pgpass>'
        , 'sslmode': 'Whether to use SSL - <disable|allow|require|...>',
        'underscore': 'Convert _ to .', 'extended':
        'Enable collection of extended database stats.', 'metrics':
        'List of enabled metrics to collect', 'pg_version':
        "The version of postgres that you'll be monitoring eg. in format 9.2",
        'has_admin': 'Admin privileges are required to execute some queries.'})
    return config_help
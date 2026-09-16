def user_exists(username, domain='', database=None, **kwargs):
    if domain:
        username = '{0}\\{1}'.format(domain, username)
    if database:
        kwargs['database'] = database
    return len(tsql_query(query=
        "SELECT name FROM sysusers WHERE name='{0}'".format(username), **
        kwargs)) == 1
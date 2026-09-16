def user_create(name, passwd, database=None, user=None, password=None, host
    =None, port=None):
    if user_exists(name, database, user, password, host, port):
        if database:
            log.info("User '%s' already exists for DB '%s'", name, database)
        else:
            log.info("Cluster admin '%s' already exists", name)
        return False
    client = _client(user=user, password=password, host=host, port=port)
    if not database:
        return client.add_cluster_admin(name, passwd)
    client.switch_database(database)
    return client.add_database_user(name, passwd)
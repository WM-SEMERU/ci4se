def get_installed_extension(name, user=None, host=None, port=None,
    maintenance_db=None, password=None, runas=None):
    return installed_extensions(user=user, host=host, port=port,
        maintenance_db=maintenance_db, password=password, runas=runas).get(name
        , None)
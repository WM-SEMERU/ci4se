def create_metadata(name, ext_version=None, schema=None, user=None, host=
    None, port=None, maintenance_db=None, password=None, runas=None):
    installed_ext = get_installed_extension(name, user=user, host=host,
        port=port, maintenance_db=maintenance_db, password=password, runas=
        runas)
    ret = [_EXTENSION_NOT_INSTALLED]
    if installed_ext:
        ret = [_EXTENSION_INSTALLED]
        if ext_version is not None and _pg_is_older_ext_ver(installed_ext.
            get('extversion', ext_version), ext_version):
            ret.append(_EXTENSION_TO_UPGRADE)
        if schema is not None and installed_ext.get('extrelocatable', 'f'
            ) == 't' and installed_ext.get('schema_name', schema) != schema:
            ret.append(_EXTENSION_TO_MOVE)
    return ret
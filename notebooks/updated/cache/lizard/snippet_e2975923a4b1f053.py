def get_module_ident_from_ident_hash(ident_hash, cursor):
    try:
        uuid, (mj_ver, mn_ver) = split_ident_hash(ident_hash, split_version
            =True)
    except IdentHashMissingVersion as e:
        uuid, mj_ver, mn_ver = e.id, None, None
    args = [uuid]
    stmt = 'SELECT module_ident FROM {} WHERE uuid = %s'
    table_name = 'modules'
    if mj_ver is None:
        table_name = 'latest_modules'
    else:
        args.append(mj_ver)
        stmt += ' AND major_version = %s'
    if mn_ver is not None:
        args.append(mn_ver)
        stmt += ' AND minor_version = %s'
    stmt = stmt.format(table_name)
    cursor.execute(stmt, args)
    try:
        module_ident = cursor.fetchone()[0]
    except TypeError:
        module_ident = None
    return module_ident
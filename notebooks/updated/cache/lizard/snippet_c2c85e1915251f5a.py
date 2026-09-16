def namedb_open(path):
    con = sqlite3.connect(path, isolation_level=None, timeout=2 ** 30)
    db_query_execute(con, 'pragma mmap_size=536870912', ())
    con.row_factory = namedb_row_factory
    version = namedb_get_version(con)
    if not semver_equal(version, VERSION):
        raise Exception(
            'Database has version {}, but this node is version {}.  Please update your node database (such as with fast_sync).'
            .format(version, VERSION))
    return con
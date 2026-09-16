def check_version_info(conn, version_table, expected_version):
    version_from_table = conn.execute(sa.select((version_table.c.version,))
        ).scalar()
    if version_from_table is None:
        version_from_table = 0
    if version_from_table != expected_version:
        raise AssetDBVersionError(db_version=version_from_table,
            expected_version=expected_version)
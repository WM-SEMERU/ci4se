def create_global_secondary_index(table_name, global_index, region=None,
    key=None, keyid=None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    table = Table(table_name, connection=conn)
    return table.create_global_secondary_index(global_index)
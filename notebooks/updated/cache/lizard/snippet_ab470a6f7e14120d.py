def create_table(table_name, region=None, key=None, keyid=None, profile=
    None, read_capacity_units=None, write_capacity_units=None, hash_key=
    None, hash_key_data_type=None, range_key=None, range_key_data_type=None,
    local_indexes=None, global_indexes=None):
    schema = []
    primary_index_fields = []
    primary_index_name = ''
    if hash_key:
        hash_key_obj = HashKey(hash_key, data_type=hash_key_data_type)
        schema.append(hash_key_obj)
        primary_index_fields.append(hash_key_obj)
        primary_index_name += hash_key
    if range_key:
        range_key_obj = RangeKey(range_key, data_type=range_key_data_type)
        schema.append(range_key_obj)
        primary_index_fields.append(range_key_obj)
        primary_index_name += '_'
        primary_index_name += range_key
    primary_index_name += '_index'
    throughput = {'read': read_capacity_units, 'write': write_capacity_units}
    local_table_indexes = []
    if local_indexes:
        for index in local_indexes:
            local_table_indexes.append(extract_index(index))
    global_table_indexes = []
    if global_indexes:
        for index in global_indexes:
            global_table_indexes.append(extract_index(index, global_index=True)
                )
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    Table.create(table_name, schema=schema, throughput=throughput, indexes=
        local_table_indexes, global_indexes=global_table_indexes,
        connection=conn)
    MAX_ATTEMPTS = 30
    for i in range(MAX_ATTEMPTS):
        if exists(table_name, region, key, keyid, profile):
            return True
        else:
            time.sleep(1)
    return False
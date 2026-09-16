def calculate_size(username, password, uuid, owner_uuid,
    is_owner_connection, client_type, serialization_version,
    client_hazelcast_version):
    data_size = 0
    data_size += calculate_size_str(username)
    data_size += calculate_size_str(password)
    data_size += BOOLEAN_SIZE_IN_BYTES
    if uuid is not None:
        data_size += calculate_size_str(uuid)
    data_size += BOOLEAN_SIZE_IN_BYTES
    if owner_uuid is not None:
        data_size += calculate_size_str(owner_uuid)
    data_size += BOOLEAN_SIZE_IN_BYTES
    data_size += calculate_size_str(client_type)
    data_size += BYTE_SIZE_IN_BYTES
    data_size += calculate_size_str(client_hazelcast_version)
    return data_size
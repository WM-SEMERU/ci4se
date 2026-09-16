def calculate_size(uuid, partition_id, interrupt):
    data_size = 0
    data_size += calculate_size_str(uuid)
    data_size += INT_SIZE_IN_BYTES
    data_size += BOOLEAN_SIZE_IN_BYTES
    return data_size
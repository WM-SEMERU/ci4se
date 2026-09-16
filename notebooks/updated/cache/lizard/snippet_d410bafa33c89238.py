def decode_response(client_message, to_object=None):
    parameters = dict(partitions=None)
    partitions_size = client_message.read_int()
    partitions = {}
    for _ in range(0, partitions_size):
        partitions_key = AddressCodec.decode(client_message, to_object)
        partitions_val_size = client_message.read_int()
        partitions_val = []
        for _ in range(0, partitions_val_size):
            partitions_val_item = client_message.read_int()
            partitions_val.append(partitions_val_item)
        partitions[partitions_key] = partitions_val
    parameters['partitions'] = partitions
    return parameters
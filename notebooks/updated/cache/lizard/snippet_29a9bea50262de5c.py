def encode_request(uuid, partition_id, interrupt):
    client_message = ClientMessage(payload_size=calculate_size(uuid,
        partition_id, interrupt))
    client_message.set_message_type(REQUEST_TYPE)
    client_message.set_retryable(RETRYABLE)
    client_message.append_str(uuid)
    client_message.append_int(partition_id)
    client_message.append_bool(interrupt)
    client_message.update_frame_length()
    return client_message
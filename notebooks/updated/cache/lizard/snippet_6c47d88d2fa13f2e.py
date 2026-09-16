def encode_request(name, entries):
    client_message = ClientMessage(payload_size=calculate_size(name, entries))
    client_message.set_message_type(REQUEST_TYPE)
    client_message.set_retryable(RETRYABLE)
    client_message.append_str(name)
    client_message.append_int(len(entries))
    for key, value in six.iteritems(entries):
        client_message.append_data(key)
        client_message.append_data(value)
    client_message.update_frame_length()
    return client_message
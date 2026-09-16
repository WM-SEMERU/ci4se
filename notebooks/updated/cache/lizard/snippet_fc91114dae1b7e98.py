def _from_binary_objid(cls, binary_stream):
    uid_size = ObjectID._UUID_SIZE
    uids = [(UUID(bytes_le=binary_stream[i * uid_size:(i + 1) * uid_size].
        tobytes()) if i * uid_size < len(binary_stream) else None) for i in
        range(0, 4)]
    _MOD_LOGGER.debug(
        'Attempted to unpack OBJECT_ID Entry from "%s"\nResult: %s',
        binary_stream.tobytes(), uids)
    return cls(uids)
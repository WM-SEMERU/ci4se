def deserialize_header_auth(stream, algorithm, verifier=None):
    _LOGGER.debug('Starting header auth deserialization')
    format_string = '>{iv_len}s{tag_len}s'.format(iv_len=algorithm.iv_len,
        tag_len=algorithm.tag_len)
    return MessageHeaderAuthentication(*unpack_values(format_string, stream,
        verifier))
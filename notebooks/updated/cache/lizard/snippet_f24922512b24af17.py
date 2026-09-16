def deserialize_footer(stream, verifier=None):
    _LOGGER.debug('Starting footer deserialization')
    signature = b''
    if verifier is None:
        return MessageFooter(signature=signature)
    try:
        sig_len, = unpack_values('>H', stream)
        signature, = unpack_values('>{sig_len}s'.format(sig_len=sig_len),
            stream)
    except SerializationError:
        raise SerializationError('No signature found in message')
    if verifier:
        verifier.verify(signature)
    return MessageFooter(signature=signature)
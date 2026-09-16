def crypto_sign_open(signed, pk):
    message = ffi.new('unsigned char[]', len(signed))
    message_len = ffi.new('unsigned long long *')
    if lib.crypto_sign_open(message, message_len, signed, len(signed), pk
        ) != 0:
        raise exc.BadSignatureError('Signature was forged or corrupt')
    return ffi.buffer(message, message_len[0])[:]
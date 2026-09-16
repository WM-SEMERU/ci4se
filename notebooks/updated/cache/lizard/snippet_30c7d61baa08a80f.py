def unserialize_data(data, compression=False, encryption=False):
    try:
        if encryption:
            data = encryption.decrypt(data)
    except Exception as err:
        logger.error('Decryption Error: ' + str(err))
        message = False
    try:
        if compression:
            data = binascii.a2b_base64(data)
            data = zlib.decompress(data)
            message = json.loads(data)
    except Exception as err:
        logger.error('Decompression Error: ' + str(err))
        message = False
    decoded_message = data.decode()
    if not encryption and not compression:
        message = json.loads(decoded_message)
    return message
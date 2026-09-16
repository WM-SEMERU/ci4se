def decrypt_filedata(data, keys):
    data.seek(-16, 2)
    tag = data.read()
    data.seek(-16, 2)
    data.truncate()
    data.seek(0)
    plain = tempfile.NamedTemporaryFile(mode='w+b', delete=False)
    pbar = progbar(fileSize(data))
    obj = Cryptodome.Cipher.AES.new(keys.encryptKey, Cryptodome.Cipher.AES.
        MODE_GCM, keys.encryptIV)
    prev_chunk = b''
    for chunk in iter(lambda : data.read(CHUNK_SIZE), b''):
        plain.write(obj.decrypt(prev_chunk))
        pbar.update(len(chunk))
        prev_chunk = chunk
    plain.write(obj.decrypt_and_verify(prev_chunk, tag))
    data.close()
    pbar.close()
    plain.seek(0)
    return plain
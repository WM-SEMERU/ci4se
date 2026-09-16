def loads(cls, data, store_password, try_decrypt_keys=True):
    try:
        pos = 0
        version = b4.unpack_from(data, pos)[0]
        pos += 4
        if version not in [1, 2]:
            raise UnsupportedKeystoreVersionException(
                'Unsupported BKS keystore version; only V1 and V2 supported, found v'
                 + repr(version))
        salt, pos = cls._read_data(data, pos)
        iteration_count = b4.unpack_from(data, pos)[0]
        pos += 4
        store_type = 'bks'
        entries, size = cls._load_bks_entries(data[pos:], store_type,
            store_password, try_decrypt_keys=try_decrypt_keys)
        hmac_fn = hashlib.sha1
        hmac_digest_size = hmac_fn().digest_size
        hmac_key_size = (hmac_digest_size * 8 if version != 1 else
            hmac_digest_size)
        hmac_key = rfc7292.derive_key(hmac_fn, rfc7292.PURPOSE_MAC_MATERIAL,
            store_password, salt, iteration_count, hmac_key_size // 8)
        store_data = data[pos:pos + size]
        store_hmac = data[pos + size:pos + size + hmac_digest_size]
        if len(store_hmac) != hmac_digest_size:
            raise BadKeystoreFormatException(
                'Bad HMAC size; found %d bytes, expected %d bytes' % (len(
                store_hmac), hmac_digest_size))
        hmac = HMAC.new(hmac_key, digestmod=SHA)
        hmac.update(store_data)
        computed_hmac = hmac.digest()
        if store_hmac != computed_hmac:
            raise KeystoreSignatureException(
                'Hash mismatch; incorrect keystore password?')
        return cls(store_type, entries, version=version)
    except struct.error as e:
        raise BadKeystoreFormatException(e)
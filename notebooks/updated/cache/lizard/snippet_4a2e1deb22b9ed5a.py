def _extract_encryption_metadata(entity, require_encryption,
    key_encryption_key, key_resolver):
    _validate_not_none('entity', entity)
    try:
        encrypted_properties_list = _decode_base64_to_bytes(entity[
            '_ClientEncryptionMetadata2'])
        encryption_data = entity['_ClientEncryptionMetadata1']
        encryption_data = _dict_to_encryption_data(loads(encryption_data))
    except Exception as e:
        if require_encryption:
            raise ValueError(_ERROR_ENTITY_NOT_ENCRYPTED)
        else:
            return None, None, None, None
    if (not encryption_data.encryption_agent.encryption_algorithm ==
        _EncryptionAlgorithm.AES_CBC_256):
        raise ValueError(_ERROR_UNSUPPORTED_ENCRYPTION_ALGORITHM)
    content_encryption_key = _validate_and_unwrap_cek(encryption_data,
        key_encryption_key, key_resolver)
    isJavaV1 = (encryption_data.key_wrapping_metadata is None or 
        encryption_data.encryption_agent.protocol ==
        _ENCRYPTION_PROTOCOL_V1 and 'EncryptionLibrary' in encryption_data.
        key_wrapping_metadata and 'Java' in encryption_data.
        key_wrapping_metadata['EncryptionLibrary'])
    metadataIV = _generate_property_iv(encryption_data.
        content_encryption_IV, entity['PartitionKey'], entity['RowKey'],
        '_ClientEncryptionMetadata2', isJavaV1)
    cipher = _generate_AES_CBC_cipher(content_encryption_key, metadataIV)
    decryptor = cipher.decryptor()
    encrypted_properties_list = decryptor.update(encrypted_properties_list
        ) + decryptor.finalize()
    unpadder = PKCS7(128).unpadder()
    encrypted_properties_list = unpadder.update(encrypted_properties_list
        ) + unpadder.finalize()
    encrypted_properties_list = encrypted_properties_list.decode('utf-8')
    if isJavaV1:
        encrypted_properties_list = encrypted_properties_list[1:-1]
        encrypted_properties_list = encrypted_properties_list.split(', ')
    else:
        encrypted_properties_list = loads(encrypted_properties_list)
    return (encryption_data.content_encryption_IV,
        encrypted_properties_list, content_encryption_key, isJavaV1)
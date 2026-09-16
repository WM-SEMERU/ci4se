def _decrypt_entity(entity, encrypted_properties_list,
    content_encryption_key, entityIV, isJavaV1):
    _validate_not_none('entity', entity)
    decrypted_entity = deepcopy(entity)
    try:
        for property in entity.keys():
            if property in encrypted_properties_list:
                value = entity[property]
                propertyIV = _generate_property_iv(entityIV, entity[
                    'PartitionKey'], entity['RowKey'], property, isJavaV1)
                cipher = _generate_AES_CBC_cipher(content_encryption_key,
                    propertyIV)
                decryptor = cipher.decryptor()
                decrypted_data = decryptor.update(value.value
                    ) + decryptor.finalize()
                unpadder = PKCS7(128).unpadder()
                decrypted_data = unpadder.update(decrypted_data
                    ) + unpadder.finalize()
                decrypted_data = decrypted_data.decode('utf-8')
                decrypted_entity[property] = decrypted_data
        decrypted_entity.pop('_ClientEncryptionMetadata1')
        decrypted_entity.pop('_ClientEncryptionMetadata2')
        return decrypted_entity
    except:
        raise AzureException(_ERROR_DECRYPTION_FAILURE)
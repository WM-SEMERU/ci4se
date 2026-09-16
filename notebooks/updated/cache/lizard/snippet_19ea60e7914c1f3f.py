def _encrypt_data_key(self, data_key, algorithm, encryption_context=None):
    kms_params = {'KeyId': self._key_id, 'Plaintext': data_key.data_key}
    if encryption_context:
        kms_params['EncryptionContext'] = encryption_context
    if self.config.grant_tokens:
        kms_params['GrantTokens'] = self.config.grant_tokens
    try:
        response = self.config.client.encrypt(**kms_params)
        ciphertext = response['CiphertextBlob']
        key_id = response['KeyId']
    except (ClientError, KeyError):
        error_message = ('Master Key {key_id} unable to encrypt data key'.
            format(key_id=self._key_id))
        _LOGGER.exception(error_message)
        raise EncryptKeyError(error_message)
    return EncryptedDataKey(key_provider=MasterKeyInfo(provider_id=self.
        provider_id, key_info=key_id), encrypted_data_key=ciphertext)
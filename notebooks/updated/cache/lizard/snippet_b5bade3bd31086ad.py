def get_secret(self, secure_data_path, key, version=None):
    warnings.warn('get_secret is deprecated, use get_secrets_data instead',
        DeprecationWarning)
    secret_resp_json = self._get_secrets(secure_data_path, version)
    if key in secret_resp_json['data']:
        return secret_resp_json['data'][key]
    else:
        raise CerberusClientException("Key '%s' not found" % key)
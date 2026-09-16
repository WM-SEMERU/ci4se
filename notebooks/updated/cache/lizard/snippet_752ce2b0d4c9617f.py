def default_kms_key_name(self, value):
    encryption_config = self._properties.get('encryption', {})
    encryption_config['defaultKmsKeyName'] = value
    self._patch_property('encryption', encryption_config)
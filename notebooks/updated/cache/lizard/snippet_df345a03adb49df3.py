def register_extension_license(self, extension_license_data):
    content = self._serialize.body(extension_license_data,
        'ExtensionLicenseData')
    response = self._send(http_method='POST', location_id=
        '004a420a-7bef-4b7f-8a50-22975d2067cc', version='5.0-preview.1',
        content=content)
    return self._deserialize('bool', response)
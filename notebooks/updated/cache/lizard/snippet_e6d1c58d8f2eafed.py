def set_license(self, key):
    data = {'LicenseKey': key}
    license_service_uri = utils.get_subresource_path_by(self, ['Oem', 'Hpe',
        'Links', 'LicenseService'])
    self._conn.post(license_service_uri, data=data)
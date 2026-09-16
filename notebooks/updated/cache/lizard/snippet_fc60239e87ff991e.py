def create_bulk_device_enrollment(self, enrollment_identities, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.create_bulk_device_enrollment_with_http_info(
            enrollment_identities, **kwargs)
    else:
        data = self.create_bulk_device_enrollment_with_http_info(
            enrollment_identities, **kwargs)
        return data
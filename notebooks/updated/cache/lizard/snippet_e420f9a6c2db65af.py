def firmware_image_create(self, datafile, name, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.firmware_image_create_with_http_info(datafile, name, **
            kwargs)
    else:
        data = self.firmware_image_create_with_http_info(datafile, name, **
            kwargs)
        return data
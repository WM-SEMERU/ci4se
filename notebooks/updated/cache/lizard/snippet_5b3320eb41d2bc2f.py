def replace_volume_attachment_status(self, name, body, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.replace_volume_attachment_status_with_http_info(name,
            body, **kwargs)
    else:
        data = self.replace_volume_attachment_status_with_http_info(name,
            body, **kwargs)
        return data
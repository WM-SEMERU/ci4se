def cancel(self, build_record_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('callback'):
        return self.cancel_with_http_info(build_record_id, **kwargs)
    else:
        data = self.cancel_with_http_info(build_record_id, **kwargs)
        return data
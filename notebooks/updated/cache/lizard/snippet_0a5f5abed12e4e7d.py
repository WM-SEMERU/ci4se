def update_event(self, id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.update_event_with_http_info(id, **kwargs)
    else:
        data = self.update_event_with_http_info(id, **kwargs)
        return data
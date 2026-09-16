def user_read_message(self, id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.user_read_message_with_http_info(id, **kwargs)
    else:
        data = self.user_read_message_with_http_info(id, **kwargs)
        return data
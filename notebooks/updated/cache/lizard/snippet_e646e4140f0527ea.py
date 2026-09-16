def long_poll_notifications(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.long_poll_notifications_with_http_info(**kwargs)
    else:
        data = self.long_poll_notifications_with_http_info(**kwargs)
        return data
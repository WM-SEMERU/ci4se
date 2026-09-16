def get_alert_history(self, id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.get_alert_history_with_http_info(id, **kwargs)
    else:
        data = self.get_alert_history_with_http_info(id, **kwargs)
        return data
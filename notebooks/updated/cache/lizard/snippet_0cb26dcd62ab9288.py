def get_group_summary(self, group_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.get_group_summary_with_http_info(group_id, **kwargs)
    else:
        data = self.get_group_summary_with_http_info(group_id, **kwargs)
        return data
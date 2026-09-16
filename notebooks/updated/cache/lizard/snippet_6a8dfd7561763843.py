def add_dashboard_tag(self, id, tag_value, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.add_dashboard_tag_with_http_info(id, tag_value, **kwargs)
    else:
        data = self.add_dashboard_tag_with_http_info(id, tag_value, **kwargs)
        return data
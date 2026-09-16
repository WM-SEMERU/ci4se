def get_revisions(self, id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('callback'):
        return self.get_revisions_with_http_info(id, **kwargs)
    else:
        data = self.get_revisions_with_http_info(id, **kwargs)
        return data
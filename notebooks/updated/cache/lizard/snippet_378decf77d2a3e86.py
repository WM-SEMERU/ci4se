def close_milestone(self, id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('callback'):
        return self.close_milestone_with_http_info(id, **kwargs)
    else:
        data = self.close_milestone_with_http_info(id, **kwargs)
        return data
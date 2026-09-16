def competitions_submissions_list(self, id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.competitions_submissions_list_with_http_info(id, **kwargs)
    else:
        data = self.competitions_submissions_list_with_http_info(id, **kwargs)
        return data
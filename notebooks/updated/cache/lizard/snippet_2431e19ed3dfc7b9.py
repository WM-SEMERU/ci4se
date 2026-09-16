def list_all_states(cls, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._list_all_states_with_http_info(**kwargs)
    else:
        data = cls._list_all_states_with_http_info(**kwargs)
        return data
def replace_state_by_id(cls, state_id, state, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return cls._replace_state_by_id_with_http_info(state_id, state, **
            kwargs)
    else:
        data = cls._replace_state_by_id_with_http_info(state_id, state, **
            kwargs)
        return data
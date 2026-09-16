def transform(data_frame, **kwargs):
    norm = kwargs.get('norm', 1.0)
    axis = kwargs.get('axis', 0)
    if axis == 0:
        norm_vector = _get_norms_of_rows(data_frame, kwargs.get('method',
            'vector'))
    else:
        norm_vector = _get_norms_of_cols(data_frame, kwargs.get('method',
            'first'))
    if 'labels' in kwargs:
        if axis == 0:
            return data_frame.apply(lambda col: col * norm / norm_vector,
                axis=0), kwargs['labels'].apply(lambda col: col * norm /
                norm_vector, axis=0)
        else:
            raise ValueError(
                'label normalization incompatible with normalization by column'
                )
    elif axis == 0:
        return data_frame.apply(lambda col: col * norm / norm_vector, axis=0)
    else:
        return data_frame.apply(lambda row: row * norm / norm_vector, axis=1)
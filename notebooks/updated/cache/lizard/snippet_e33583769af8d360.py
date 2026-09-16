def _check_item_type(item, field_name, allowed_types, expect_list=False,
    required_channels='all'):
    if expect_list:
        if not isinstance(item, list):
            raise TypeError('Field `%s` must be a list.' % field_name)
        if required_channels == 'all':
            required_channels = list(range(len(item)))
        for ch in range(len(item)):
            if ch in required_channels:
                allowed_types_ch = allowed_types
            else:
                allowed_types_ch = allowed_types + (type(None),)
            if not isinstance(item[ch], allowed_types_ch):
                raise TypeError(
                    'Channel %d of field `%s` must be one of the following types:'
                     % (ch, field_name), allowed_types_ch)
    elif not isinstance(item, allowed_types):
        raise TypeError('Field `%s` must be one of the following types:',
            allowed_types)
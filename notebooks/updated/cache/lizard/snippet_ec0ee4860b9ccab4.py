def vsreenqueue(item_id, item_s, args, **kwargs):
    charset = kwargs.get('charset', _c.FSQ_CHARSET)
    if kwargs.has_key('charset'):
        del kwargs['charset']
    kwargs['item_id'] = item_id
    if isinstance(item_s, unicode):
        try:
            item_s = item_s.encode(charset)
        except UnicodeEncodeError:
            raise FSQCoerceError(errno.EINVAL,
                'cannot encode item with charset {0}'.format(charset))
    return vreenqueue(StringIO(item_s), item_id, args, **kwargs)
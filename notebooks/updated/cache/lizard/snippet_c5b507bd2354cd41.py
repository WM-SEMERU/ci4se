def _decode_data(self, data, charset):
    try:
        return smart_unicode(data, charset)
    except UnicodeDecodeError:
        raise errors.BadRequest('wrong charset')
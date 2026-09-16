def upload(self, data, callback=None, content_type=None, size=None):
    url = 'upload'
    if not hasattr(data, 'read') and not (hasattr(data, '__next__') or
        hasattr(data, 'next')):
        data = six.BytesIO(force_bytes(data))
    elif not hasattr(data, 'read') and (hasattr(data, '__next__') or
        hasattr(data, 'next')):
        if size is None:
            raise Exception('Cannot upload iterable with unknown size')
        data = ReadableIterator(data, size)
    menc = MultipartEncoder(fields={'file': ('file', data, content_type)})
    if callback is not None:
        menc = MultipartEncoderMonitor(menc, callback)
    headers = {'Content-Type': menc.content_type}
    if size:
        if not isinstance(size, six.string_types):
            size = str(size)
        headers['Content-Length'] = size
    try:
        response = self.post(url, data=menc, headers=headers)
    except OverflowError:
        msg = 'upload content larger than system maxint (32-bit OS limitation)'
        logger.error('OverflowError: %s', msg)
        raise OverflowError(msg)
    if response.status_code == requests.codes.accepted:
        return response.text.strip()
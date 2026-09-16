async def parse_result(response, response_type=None, *, encoding='utf-8'):
    if response_type is None:
        ct = response.headers.get('content-type')
        if ct is None:
            cl = response.headers.get('content-length')
            if cl is None or cl == '0':
                return ''
            raise TypeError(
                'Cannot auto-detect response type due to missing Content-Type header.'
                )
        main_type, sub_type, extras = parse_content_type(ct)
        if sub_type == 'json':
            response_type = 'json'
        elif sub_type == 'x-tar':
            response_type = 'tar'
        elif (main_type, sub_type) == ('text', 'plain'):
            response_type = 'text'
            encoding = extras.get('charset', encoding)
        else:
            raise TypeError('Unrecognized response type: {ct}'.format(ct=ct))
    if 'tar' == response_type:
        what = await response.read()
        return tarfile.open(mode='r', fileobj=BytesIO(what))
    if 'json' == response_type:
        data = await response.json(encoding=encoding)
    elif 'text' == response_type:
        data = await response.text(encoding=encoding)
    else:
        data = await response.read()
    return data
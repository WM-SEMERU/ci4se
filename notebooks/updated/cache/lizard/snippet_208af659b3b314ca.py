def text_stream(stream, content_type='text/plain; charset=utf-8', status=
    '200 OK'):
    if 'charset' not in content_type:
        content_type += '; charset=utf-8'
    return WbResponse.bin_stream(WbResponse.encode_stream(stream),
        content_type, status)
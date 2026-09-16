async def file_stream(location, status=200, chunk_size=4096, mime_type=None,
    headers=None, filename=None, _range=None):
    headers = headers or {}
    if filename:
        headers.setdefault('Content-Disposition',
            'attachment; filename="{}"'.format(filename))
    filename = filename or path.split(location)[-1]
    _file = await open_async(location, mode='rb')

    async def _streaming_fn(response):
        nonlocal _file, chunk_size
        try:
            if _range:
                chunk_size = min((_range.size, chunk_size))
                await _file.seek(_range.start)
                to_send = _range.size
                while to_send > 0:
                    content = await _file.read(chunk_size)
                    if len(content) < 1:
                        break
                    to_send -= len(content)
                    await response.write(content)
            else:
                while True:
                    content = await _file.read(chunk_size)
                    if len(content) < 1:
                        break
                    await response.write(content)
        finally:
            await _file.close()
        return
    mime_type = mime_type or guess_type(filename)[0] or 'text/plain'
    if _range:
        headers['Content-Range'] = 'bytes %s-%s/%s' % (_range.start, _range
            .end, _range.total)
        status = 206
    return StreamingHTTPResponse(streaming_fn=_streaming_fn, status=status,
        headers=headers, content_type=mime_type)
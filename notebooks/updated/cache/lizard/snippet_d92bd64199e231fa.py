def parse_content_stream(page_or_stream, operators=''):
    if not isinstance(page_or_stream, Object):
        raise TypeError('stream must a PDF object')
    if page_or_stream._type_code != ObjectType.stream and page_or_stream.get(
        '/Type') != '/Page':
        raise TypeError('parse_content_stream called on page or stream object')
    try:
        if page_or_stream.get('/Type') == '/Page':
            page = page_or_stream
            instructions = page._parse_page_contents_grouped(operators)
        else:
            stream = page_or_stream
            instructions = Object._parse_stream_grouped(stream, operators)
    except PdfError as e:
        if 'ignoring non-stream while parsing' in str(e):
            raise TypeError('parse_content_stream called on non-stream Object')
        raise e from e
    return instructions
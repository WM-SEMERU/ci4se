def encode_multipart_formdata(fields, boundary=None, charset=None):
    charset = charset or 'utf-8'
    body = BytesIO()
    if boundary is None:
        boundary = choose_boundary()
    for fieldname, value in mapping_iterator(fields):
        body.write(('--%s\r\n' % boundary).encode(charset))
        if isinstance(value, tuple):
            filename, data = value
            body.write((
                'Content-Disposition: form-data; name="%s"; filename="%s"\r\n'
                 % (fieldname, filename)).encode(charset))
            body.write(('Content-Type: %s\r\n\r\n' % get_content_type(
                filename)).encode(charset))
        else:
            data = value
            body.write(('Content-Disposition: form-data; name="%s"\r\n' %
                fieldname).encode(charset))
            body.write(b'Content-Type: text/plain\r\n\r\n')
        body.write(to_bytes(data))
        body.write(b'\r\n')
    body.write(('--%s--\r\n' % boundary).encode(charset))
    content_type = 'multipart/form-data; boundary=%s' % boundary
    return body.getvalue(), content_type
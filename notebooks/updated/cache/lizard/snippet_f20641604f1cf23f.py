def _convert_batch_to_json(batch_requests):
    batch_boundary = b'batch_' + _new_boundary()
    changeset_boundary = b'changeset_' + _new_boundary()
    body = [b'--' + batch_boundary + b'\n',
        b'Content-Type: multipart/mixed; boundary=', changeset_boundary +
        b'\n\n']
    content_id = 1
    for _, request in batch_requests:
        body.append(b'--' + changeset_boundary + b'\n')
        body.append(b'Content-Type: application/http\n')
        body.append(b'Content-Transfer-Encoding: binary\n\n')
        body.append(request.method.encode('utf-8'))
        body.append(b' ')
        body.append(request.path.encode('utf-8'))
        body.append(b' HTTP/1.1\n')
        body.append(b'Content-ID: ')
        body.append(str(content_id).encode('utf-8') + b'\n')
        content_id += 1
        for name, value in request.headers.items():
            if name in _SUB_HEADERS:
                body.append(name.encode('utf-8') + b': ')
                body.append(value.encode('utf-8') + b'\n')
        if not request.method == 'DELETE':
            body.append(b'Content-Length: ')
            body.append(str(len(request.body)).encode('utf-8'))
            body.append(b'\n\n')
            body.append(request.body + b'\n')
        body.append(b'\n')
    body.append(b'--' + changeset_boundary + b'--' + b'\n')
    body.append(b'--' + batch_boundary + b'--')
    return b''.join(body
        ), 'multipart/mixed; boundary=' + batch_boundary.decode('utf-8')
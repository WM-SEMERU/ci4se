def get_resource(request, resource, allow_multiple=False, full_clean=True,
    default_to_not_supplied=False):
    body = request.body
    if isinstance(body, bytes):
        try:
            body = body.decode('UTF8')
        except UnicodeDecodeError as ude:
            raise HttpError(HTTPStatus.BAD_REQUEST, 99,
                'Unable to decode request body.', str(ude))
    try:
        instance = request.request_codec.loads(body, resource=resource,
            full_clean=full_clean, default_to_not_supplied=
            default_to_not_supplied)
    except ResourceException:
        raise HttpError(HTTPStatus.BAD_REQUEST, 98, 'Invalid resource type.')
    except CodecDecodeError as cde:
        raise HttpError(HTTPStatus.BAD_REQUEST, 96,
            'Unable to decode body.', str(cde))
    if isinstance(instance, list):
        if any(not isinstance(i, resource) for i in instance):
            raise HttpError(HTTPStatus.BAD_REQUEST, 98,
                'Invalid resource type.')
        if not allow_multiple:
            raise HttpError(HTTPStatus.BAD_REQUEST, 97,
                'Expected a single resource not a list.')
    elif not isinstance(instance, resource):
        raise HttpError(HTTPStatus.BAD_REQUEST, 98, 'Invalid resource type.')
    return instance
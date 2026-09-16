def get_header(request, header_service):
    service = request.META.get('HTTP_{}'.format(header_service), b'')
    if isinstance(service, str):
        service = service.encode(HTTP_HEADER_ENCODING)
    return service
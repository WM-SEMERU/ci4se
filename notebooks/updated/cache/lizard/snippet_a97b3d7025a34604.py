def serve_private_file(request, path):
    logger.debug('Serving {0} to {1}'.format(path, request.user))
    if not permissions.has_read_permission(request, path):
        if settings.DEBUG:
            raise PermissionDenied
        else:
            raise Http404('File not found')
    return server.serve(request, path=path)
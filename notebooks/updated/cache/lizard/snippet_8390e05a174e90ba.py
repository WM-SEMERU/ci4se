def csrf_protect_all_post_and_cross_origin_requests():
    success = None
    if is_cross_origin(request):
        logger.warning('Received cross origin request. Aborting')
        abort(403)
    if request.method in ['POST', 'PUT']:
        token = session.get('csrf_token')
        if token == request.form.get('csrf_token'):
            return success
        elif token == request.environ.get('HTTP_X_CSRFTOKEN'):
            return success
        else:
            logger.warning('Received invalid csrf token. Aborting')
            abort(403)
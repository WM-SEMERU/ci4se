def process_request(self, request):
    if COOKIE_KEY in request.COOKIES and request.COOKIES[COOKIE_KEY
        ] == COOKIE_SPAM:
        response = HttpResponse('')
        response.status_code = 404
        if DJANGOSPAM_LOG:
            logger.log('SPAM REQUEST', request.method, request.path_info,
                request.META.get('HTTP_USER_AGENT', 'undefined'))
        return response
    if DJANGOSPAM_LOG:
        logger.log('PASS REQUEST', request.method, request.path_info,
            request.META.get('HTTP_USER_AGENT', 'undefined'))
    return None
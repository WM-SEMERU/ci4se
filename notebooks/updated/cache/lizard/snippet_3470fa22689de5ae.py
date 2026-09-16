def process_response(self, request, response):
    if hasattr(request, 'COUNTRY_CODE'):
        response.set_cookie(key=constants.COUNTRY_COOKIE_NAME, value=
            request.COUNTRY_CODE, max_age=settings.LANGUAGE_COOKIE_AGE,
            path=settings.LANGUAGE_COOKIE_PATH, domain=settings.
            LANGUAGE_COOKIE_DOMAIN)
    return response
def process_exception(self, request, exception):
    if isinstance(exception, (exceptions.NotAuthorized, exceptions.
        NotAuthenticated)):
        auth_url = settings.LOGIN_URL
        next_url = None
        if request.method in ('POST', 'PUT'):
            referrer = request.META.get('HTTP_REFERER')
            if referrer and is_safe_url(referrer, request.get_host()):
                next_url = referrer
        if not next_url:
            next_url = iri_to_uri(request.get_full_path())
        if next_url != auth_url:
            field_name = REDIRECT_FIELD_NAME
        else:
            field_name = None
        login_url = request.build_absolute_uri(auth_url)
        response = redirect_to_login(next_url, login_url=login_url,
            redirect_field_name=field_name)
        if isinstance(exception, exceptions.NotAuthorized):
            logout_reason = _('Unauthorized. Please try logging in again.')
            utils.add_logout_reason(request, response, logout_reason)
            response.delete_cookie('messages')
        if request.is_ajax():
            response_401 = http.HttpResponse(status=401)
            response_401['X-Horizon-Location'] = response['location']
            return response_401
        return response
    if isinstance(exception, exceptions.NotFound):
        raise http.Http404(exception)
    if isinstance(exception, exceptions.Http302):
        return shortcuts.redirect(exception.location)
def process_request(self, request):
    assert hasattr(request, 'user')
    if not request.user.is_authenticated():
        path = request.path_info.lstrip('/')
        if not any(m.match(path) for m in EXEMPT_URLS):
            return HttpResponseRedirect(reverse(settings.LOGIN_URL))
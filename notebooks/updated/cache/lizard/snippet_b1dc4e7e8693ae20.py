def set_locale(request):
    return request.query.get('lang', app.ps.babel.select_locale_by_request(
        request))
def clear_profiling_cookies(request, response):
    if 'profile_page' in request.COOKIES:
        path = request.path
        response.set_cookie('profile_page', max_age=0, path=path)
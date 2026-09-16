def watch_login(status_code=302, msg='', get_username=utils.
    get_username_from_request):

    def decorated_login(func):

        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            if utils.is_already_locked(request):
                return utils.lockout_response(request)
            response = func(request, *args, **kwargs)
            if request.method == 'POST':
                if status_code == 302:
                    login_unsuccessful = response and not response.has_header(
                        'location') and response.status_code != status_code
                else:
                    login_unsuccessful = (response and response.status_code ==
                        status_code and msg in response.content.decode('utf-8')
                        )
                utils.add_login_attempt_to_db(request, not
                    login_unsuccessful, get_username)
                if utils.check_request(request, login_unsuccessful,
                    get_username):
                    return response
                return utils.lockout_response(request)
            return response
        return wrapper
    return decorated_login
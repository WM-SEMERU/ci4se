def authenticator(function, challenges=()):
    challenges = challenges or ('{} realm="simple"'.format(function.__name__),)

    def wrapper(verify_user):

        def authenticate(request, response, **kwargs):
            result = function(request, response, verify_user, **kwargs)

            def authenticator_name():
                try:
                    return function.__doc__.splitlines()[0]
                except AttributeError:
                    return function.__name__
            if result is None:
                raise HTTPUnauthorized('Authentication Required',
                    'Please provide valid {0} credentials'.format(
                    authenticator_name()), challenges=challenges)
            if result is False:
                raise HTTPUnauthorized('Invalid Authentication',
                    'Provided {0} credentials were invalid'.format(
                    authenticator_name()), challenges=challenges)
            request.context['user'] = result
            return True
        authenticate.__doc__ = function.__doc__
        return authenticate
    return wrapper
def _api_call(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            if not _webview_ready.wait(15):
                raise Exception('Main window failed to start')
            return function(*args, **kwargs)
        except NameError:
            raise Exception(
                'Create a web view window first, before invoking this function'
                )
        except KeyError as e:
            try:
                uid = kwargs['uid']
            except KeyError:
                uid = args[-1]
            raise Exception(
                'Cannot call function: No webview exists with uid: {}'.
                format(uid))
    return wrapper
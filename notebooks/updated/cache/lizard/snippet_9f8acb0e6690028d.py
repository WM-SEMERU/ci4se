def process_exception(self, request: AxesHttpRequest, exception):
    if isinstance(exception, AxesSignalPermissionDenied):
        return get_lockout_response(request)
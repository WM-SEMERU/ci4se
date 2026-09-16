def _do_request(self, method, *args, **kwargs):
    log('Doing HTTP [{3}] request: {0} - headers: {1} - payload: {2}'.
        format(args[0], kwargs.get('headers'), kwargs.get('json'), method),
        level=logging.DEBUG)
    requests_method = getattr(requests, method)
    return self._handle_response(requests_method(*args, **kwargs))
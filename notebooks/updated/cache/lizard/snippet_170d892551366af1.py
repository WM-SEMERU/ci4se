def xross_view(*op_functions):
    operations_dict = construct_operations_dict(*op_functions)

    def get_request(src):
        return src if isinstance(src, HttpRequest) else None

    def dec_wrapper(func):

        def func_wrapper(*fargs, **fkwargs):
            request_idx = getattr(func, '_req_idx', None)
            if request_idx is None:
                request = get_request(fargs[0])
                request_idx = 0
                if not request:
                    request = get_request(fargs[1])
                    request_idx = 1
                func._req_idx = request_idx
            else:
                request = fargs[request_idx]
            if hasattr(request, '_xross_handler'):
                request._xross_handler._op_bindings.update(operations_dict[
                    '_op_bindings'])
            else:
                request._xross_handler = build_handler_class(operations_dict)(
                    request, func)
            try:
                response = func(*fargs, **fkwargs)
            except HandlerException as e:
                return HttpResponseBadRequest(e if settings.DEBUG else b'')
            except ResponseEmpty as e:
                return HttpResponseNotFound(e if settings.DEBUG else b'')
            except ResponseReady as r:
                response = r.response
                if response is None:
                    response = ''
                if isinstance(response, str):
                    response = HttpResponse(response)
                elif isinstance(response, dict):
                    response = HttpResponse(json.dumps(response),
                        content_type='application/json')
            return response
        return func_wrapper
    return dec_wrapper
def response_middleware(api=None):

    def decorator(middleware_method):
        apply_to_api = hug.API(api) if api else hug.api.from_object(
            middleware_method)


        class MiddlewareRouter(object):
            __slots__ = ()

            def process_response(self, request, response, resource,
                req_succeeded):
                return middleware_method(request, response, resource)
        apply_to_api.http.add_middleware(MiddlewareRouter())
        return middleware_method
    return decorator
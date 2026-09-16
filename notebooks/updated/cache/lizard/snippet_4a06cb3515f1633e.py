def middleware_class(api=None):

    def decorator(middleware_class):
        apply_to_api = hug.API(api) if api else hug.api.from_object(
            middleware_class)
        apply_to_api.http.add_middleware(middleware_class())
        return middleware_class
    return decorator
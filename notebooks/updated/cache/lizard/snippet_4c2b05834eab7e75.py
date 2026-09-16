def patch_loader(*decorator_args, serializer):

    def wrapped(fn):

        @wraps(fn)
        def decorated(*args, **kwargs):
            result = serializer.load(request.get_json(), instance=kwargs.
                pop('instance'), partial=True)
            if not result.errors and not result.data.id:
                abort(HTTPStatus.NOT_FOUND)
            return fn(*result)
        return decorated
    if decorator_args and callable(decorator_args[0]):
        return wrapped(decorator_args[0])
    return wrapped
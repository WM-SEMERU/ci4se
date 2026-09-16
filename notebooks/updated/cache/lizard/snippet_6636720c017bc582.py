def _wrap_unary_errors(callable_):
    _patch_callable_name(callable_)

    @six.wraps(callable_)
    def error_remapped_callable(*args, **kwargs):
        try:
            return callable_(*args, **kwargs)
        except grpc.RpcError as exc:
            six.raise_from(exceptions.from_grpc_error(exc), exc)
    return error_remapped_callable
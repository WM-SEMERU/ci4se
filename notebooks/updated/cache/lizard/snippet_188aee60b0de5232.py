def Task(func, *args, **kwargs):
    future = Future()

    def handle_exception(typ, value, tb):
        if future.done():
            return False
        future.set_exc_info((typ, value, tb))
        return True

    def set_result(result):
        if future.done():
            return
        future.set_result(result)
    with stack_context.ExceptionStackContext(handle_exception):
        func(*args, callback=_argument_adapter(set_result), **kwargs)
    return future
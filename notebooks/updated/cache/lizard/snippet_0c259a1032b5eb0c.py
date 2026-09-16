def future_then_immediate(future, func):
    result = concurrent.futures.Future()

    def on_done(f):
        try:
            result.set_result(func(f.result()))
        except Exception as e:
            result.set_exception(e)
    future.add_done_callback(on_done)
    return result
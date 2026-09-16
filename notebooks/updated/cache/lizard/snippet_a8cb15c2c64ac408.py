def async_call(self, fn, *args, **kwargs):
    call_point = ''.join(format_stack(None, 5)[:-1])

    def handler():
        try:
            fn(*args, **kwargs)
        except Exception as err:
            msg = (
                """error caught while executing async callback:
{!r}
{}
 
the call was requested at
{}"""
                .format(err, format_exc_skip(1), call_point))
            self._err_cb(msg)
            raise
    self._session.threadsafe_call(handler)
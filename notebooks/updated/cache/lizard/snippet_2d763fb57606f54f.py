def partial(coro, *args, **kw):
    assert_corofunction(coro=coro)

    @asyncio.coroutine
    def wrapper(*_args, **_kw):
        call_args = args + _args
        kw.update(_kw)
        return (yield from coro(*call_args, **kw))
    return wrapper
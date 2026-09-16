def apply(coro, *args, **kw):
    assert_corofunction(coro=coro)

    @asyncio.coroutine
    def wrapper(*_args, **_kw):
        return (yield from coro(*args, **kw))
    return wrapper
async def _async_supervisor(func, animation_, step, *args, **kwargs):
    with ThreadPoolExecutor(max_workers=2) as pool:
        with _terminating_event() as event:
            pool.submit(animate_cli, animation_, step, event)
            result = await func(*args, **kwargs)
    return result
def asyncio_main_run(root_runner: BaseRunner):
    assert threading.current_thread() == threading.main_thread(
        ), 'only main thread can accept asyncio subprocesses'
    if sys.platform == 'win32':
        event_loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(event_loop)
    else:
        event_loop = asyncio.get_event_loop()
        asyncio.get_child_watcher().attach_loop(event_loop)
    event_loop.run_until_complete(awaitable_runner(root_runner))
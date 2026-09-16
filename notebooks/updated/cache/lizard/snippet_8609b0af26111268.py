async def awaitable_runner(runner: BaseRunner):
    runner_thread = CapturingThread(target=runner.run)
    runner_thread.start()
    delay = 0.0
    while not runner_thread.join(timeout=0):
        await asyncio.sleep(delay)
        delay = min(delay + 0.1, 1.0)
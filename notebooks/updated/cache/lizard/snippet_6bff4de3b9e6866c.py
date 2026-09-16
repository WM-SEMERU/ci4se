async def dataSources(loop=None, executor=None):
    loop = loop or asyncio.get_event_loop()
    sources = await loop.run_in_executor(executor, _dataSources)
    return sources
def sync_connect(self):
    loop = asyncio.get_event_loop()
    task = loop.create_task(self.connect())
    loop.run_until_complete(task)
def create_server_and_run_forever(self, loop=None, **server_config):
    if loop is None:
        import asyncio
        loop = asyncio.get_event_loop()
    self.create_server(loop=loop, **server_config)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
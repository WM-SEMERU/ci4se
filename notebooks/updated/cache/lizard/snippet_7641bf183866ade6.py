async def connect(self):
    self.pool = await aiopg.create_pool(loop=self.loop, timeout=self.
        timeout, database=self.database, **self.connect_params)
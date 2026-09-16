def i2c_read_data(self, address):
    task = asyncio.ensure_future(self.core.i2c_read_data(address))
    value = self.loop.run_until_complete(task)
    return value
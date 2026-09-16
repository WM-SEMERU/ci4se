def pixy_init(self, max_blocks=5, cb=None, cb_type=None):
    task = asyncio.ensure_future(self.core.pixy_init(max_blocks, cb, cb_type))
    self.loop.run_until_complete(task)
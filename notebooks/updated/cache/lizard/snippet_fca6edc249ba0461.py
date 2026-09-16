async def identify(self, duration_s: int=5):
    count = duration_s * 4
    on = False
    for sec in range(count):
        then = self._loop.time()
        self.set_lights(button=on)
        on = not on
        now = self._loop.time()
        await asyncio.sleep(max(0, 0.25 - (now - then)))
    self.set_lights(button=True)
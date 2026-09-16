def play_tone(self, pin, tone_command, frequency, duration=None):
    task = asyncio.ensure_future(self.core.play_tone(pin, tone_command,
        frequency, duration))
    self.loop.run_until_complete(task)
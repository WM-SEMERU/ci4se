def stepper_config(self, steps_per_revolution, stepper_pins):
    task = asyncio.ensure_future(self.core.stepper_config(
        steps_per_revolution, stepper_pins))
    self.loop.run_until_complete(task)
def attach(self, engine, start=Events.STARTED, pause=Events.COMPLETED,
    resume=None, step=None):
    engine.add_event_handler(start, self.reset)
    engine.add_event_handler(pause, self.pause)
    if resume is not None:
        engine.add_event_handler(resume, self.resume)
    if step is not None:
        engine.add_event_handler(step, self.step)
    return self
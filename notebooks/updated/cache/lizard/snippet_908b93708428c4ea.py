def do_execute(self):
    result = None
    self._stopped = False
    self._stopping = False
    for actor in self.owner.actors:
        if self.is_stopping() or self.is_stopped():
            break
        actor.input = self.owner.input
        result = actor.execute()
        if result is not None:
            break
    return result
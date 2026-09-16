def start(self, reloading=False):
    for event in self.event_handlers:
        self.controller.listen(event)
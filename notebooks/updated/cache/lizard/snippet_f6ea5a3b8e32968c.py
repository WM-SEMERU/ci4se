def start(self):
    for name, child in self._compound_children.items():
        self.logger.debug('start %s (%s)', name, child.__class__.__name__)
        child.start()
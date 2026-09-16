def _loadHandlers(self):
    return {handler.name: handler for handler in map(self.createHandler,
        self.config['handlers'])}
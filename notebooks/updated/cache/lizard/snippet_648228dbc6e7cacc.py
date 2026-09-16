def delete(self):
    self.manager.session.delete(self.uri)
    self.manager._metrics_contexts.remove(self)
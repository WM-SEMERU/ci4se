def _threads(self, handlers):
    if self.threads < len(handlers):
        return self.threads
    return len(handlers)
def busy_connections(self):
    return [c for c in self.connections.values() if c.busy and not c.closed]
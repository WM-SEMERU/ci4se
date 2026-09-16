def create_connections(self):
    self.set_state(self.STATE_CONNECTING)
    for conn in self.consumer_config.get('connections', []):
        name, confirm, consume = conn, False, True
        if isinstance(conn, dict):
            name = conn['name']
            confirm = conn.get('publisher_confirmation', False)
            consume = conn.get('consume', True)
        if name not in self.config['Connections']:
            LOGGER.critical('Connection "%s" for %s not found', name, self.
                consumer_name)
            continue
        self.connections[name] = connection.Connection(name, self.config[
            'Connections'][name], self.consumer_name, consume, confirm,
            self.ioloop, self.callbacks)
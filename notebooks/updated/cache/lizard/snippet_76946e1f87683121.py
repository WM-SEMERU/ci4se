def compute_full_connections(self, config, direct):
    hidden = [i for i in iterkeys(self.nodes) if i not in config.output_keys]
    output = [i for i in iterkeys(self.nodes) if i in config.output_keys]
    connections = []
    if hidden:
        for input_id in config.input_keys:
            for h in hidden:
                connections.append((input_id, h))
        for h in hidden:
            for output_id in output:
                connections.append((h, output_id))
    if direct or not hidden:
        for input_id in config.input_keys:
            for output_id in output:
                connections.append((input_id, output_id))
    if not config.feed_forward:
        for i in iterkeys(self.nodes):
            connections.append((i, i))
    return connections
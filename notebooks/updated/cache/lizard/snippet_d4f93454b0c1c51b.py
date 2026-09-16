def encode(self, delimiter=';'):
    try:
        return delimiter.join([str(f) for f in [self.node_id, self.child_id,
            int(self.type), self.ack, int(self.sub_type), self.payload]]
            ) + '\n'
    except ValueError:
        _LOGGER.error('Error encoding message to gateway')
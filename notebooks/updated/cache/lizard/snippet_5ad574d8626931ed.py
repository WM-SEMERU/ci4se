def sequence_id(self, sequence):
    if self.meaningful_ids:
        return '><'.join([node.id for node in sequence])
    else:
        return getrandbits(64)
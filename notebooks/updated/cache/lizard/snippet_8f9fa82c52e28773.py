def classify(self, peer_dir_meta):
    assert self.operation is None
    peer_entry_meta = peer_dir_meta.get(self.name, False
        ) if peer_dir_meta else None
    if self.local:
        self.local.classify(peer_dir_meta)
        self.local_classification = self.local.classification
    elif peer_entry_meta:
        self.local_classification = 'deleted'
    else:
        self.local_classification = 'missing'
    if self.remote:
        self.remote.classify(peer_dir_meta)
        self.remote_classification = self.remote.classification
    elif peer_entry_meta:
        self.remote_classification = 'deleted'
    else:
        self.remote_classification = 'missing'
    c_pair = self.local_classification, self.remote_classification
    self.operation = operation_map.get(c_pair)
    if not self.operation:
        raise RuntimeError('Undefined operation for pair classification {}'
            .format(c_pair))
    if PRINT_CLASSIFICATIONS:
        write('classify {}'.format(self))
    assert self.operation in PAIR_OPERATIONS
    return self.operation
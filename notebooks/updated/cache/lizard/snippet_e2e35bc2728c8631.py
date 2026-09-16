def get_by_block(self, block_number):
    blocklist_snapshot = self.db.prefixed_db(NotificationPrefix.PREFIX_BLOCK
        ).snapshot()
    block_bytes = block_number.to_bytes(4, 'little')
    results = []
    for val in blocklist_snapshot.iterator(prefix=block_bytes, include_key=
        False):
        event = SmartContractEvent.FromByteArray(val)
        results.append(event)
    return results
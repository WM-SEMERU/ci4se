def get_processing_block_ids(self):
    _processing_block_ids = []
    pattern = '*:processing_block:*'
    block_ids = self._db.get_ids(pattern)
    for block_id in block_ids:
        id_split = block_id.split(':')[-1]
        _processing_block_ids.append(id_split)
    return sorted(_processing_block_ids)
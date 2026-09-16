def _split_sched_block_instance(self, scheduling_block):
    _scheduling_block_data = {}
    _processing_block_data = {}
    _processing_block_id = []
    for block in scheduling_block:
        values = scheduling_block[block]
        if block != 'processing_blocks':
            _scheduling_block_data[block] = values
        else:
            processing_block_id = self.get_processing_block_ids()
            for value in values:
                if value['id'] not in processing_block_id:
                    _processing_block_data = values
                else:
                    raise Exception('Processing block already exits', value
                        ['id'])
    for block_id in _processing_block_data:
        _processing_block_id.append(block_id['id'])
    _scheduling_block_data['processing_block_ids'] = _processing_block_id
    return _scheduling_block_data, _processing_block_data
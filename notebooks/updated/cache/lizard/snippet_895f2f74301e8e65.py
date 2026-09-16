def rpc_get_blockstack_ops_at(self, block_id, offset, count, **con_info):
    if not check_block(block_id):
        return {'error': 'Invalid block height', 'http_status': 400}
    if not check_offset(offset):
        return {'error': 'Invalid offset', 'http_status': 400}
    if not check_count(count, 10):
        return {'error': 'Invalid count', 'http_status': 400}
    db = get_db_state(self.working_dir)
    nameops = db.get_all_blockstack_ops_at(block_id, offset=offset, count=count
        )
    db.close()
    log.debug('{} name operations at block {}, offset {}, count {}'.format(
        len(nameops), block_id, offset, count))
    ret = []
    for nameop in nameops:
        assert 'opcode' in nameop, 'BUG: missing opcode in {}'.format(json.
            dumps(nameop, sort_keys=True))
        canonical_op = self.sanitize_rec(nameop)
        ret.append(canonical_op)
    return self.success_response({'nameops': ret})
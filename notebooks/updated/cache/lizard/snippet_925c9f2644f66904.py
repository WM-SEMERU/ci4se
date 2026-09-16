def commit_state_preorder(self, nameop, current_block_number):
    if self.disposition != DISPOSITION_RW:
        log.error('FATAL: borrowing violation: not a read-write connection')
        traceback.print_stack()
        os.abort()
    opcode = None
    try:
        opcode = nameop.get('opcode')
        assert opcode is not None, 'BUG: no preorder opcode'
    except Exception as e:
        log.exception(e)
        log.error('FATAL: no opcode in preorder')
        os.abort()
    account_payment_info = state_preorder_get_account_payment_info(nameop)
    cur = self.db.cursor()
    if BlockstackDB.nameop_is_collided(nameop):
        log.debug("Not commiting '%s', since it collided" % nameop)
        self.log_reject(current_block_number, nameop['vtxindex'], nameop[
            'op'], nameop)
        return []
    self.log_accept(current_block_number, nameop['vtxindex'], nameop['op'],
        nameop)
    commit_preorder = self.sanitize_op(nameop)
    rc = namedb_preorder_insert(cur, commit_preorder)
    if not rc:
        log.error("FATAL: failed to commit preorder '%s'" % commit_preorder
            ['preorder_hash'])
        os.abort()
    self.commit_account_debit(opcode, account_payment_info,
        current_block_number, nameop['vtxindex'], nameop['txid'])
    self.db.commit()
    return commit_preorder
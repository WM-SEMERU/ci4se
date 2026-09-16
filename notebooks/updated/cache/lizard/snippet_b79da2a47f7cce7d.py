def db_setup(self):
    if self.db_exists(impl=self.impl, working_dir=self.working_dir):
        if not self.read_only and self.db_is_indexing(self.impl, self.
            working_dir):
            log.error('Unclean shutdown detected on read/write open')
            return False
    else:
        assert not self.read_only, 'Cannot instantiate database if read_only is True'
        db_con = self.db_create(self.impl, self.working_dir)
        initial_snapshots = self.impl.get_initial_snapshots()
        for block_id in sorted(initial_snapshots.keys()):
            self.db_snapshot_append(db_con, int(block_id), str(
                initial_snapshots[block_id]), None, int(time.time()))
    self.chainstate_path = config.get_snapshots_filename(self.impl, self.
        working_dir)
    self.lastblock = self.get_lastblock(self.impl, self.working_dir)
    self.setup = True
    return True
def flush_cache(self):
    logger.debug('Flushing cache {}'.format(self.db_path))
    with self.db:
        for rec in self._tups:
            self.db.execute(
                'replace into history(agent_id, t_step, key, value) values (?, ?, ?, ?)'
                , (rec.agent_id, rec.t_step, rec.key, rec.value))
    self._tups = list()
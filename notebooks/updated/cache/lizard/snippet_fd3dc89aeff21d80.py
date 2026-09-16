def _add_indices(self):
    self._logger.info('Adding database indices')
    self._conn.execute(constants.CREATE_INDEX_TEXTNGRAM_SQL)
    self._logger.info('Indices added')
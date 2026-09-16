def load(self):
    self._validate()
    self._logger.logging_load()
    formatter = MediaWikiTableFormatter(self.source)
    formatter.accept(self)
    return formatter.to_table_data()
def _pretend_to_run(self, migration, method):
    for query in self._get_queries(migration, method):
        name = migration.__class__.__name__
        self._note('<info>%s:</info> <comment>%s</comment>' % (name, query))
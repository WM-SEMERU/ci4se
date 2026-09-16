def statistics(self, catalog=None, schema=None, unique=False, quick=True):
    fut = self._run_operation(self._impl.statistics, catalog=catalog,
        schema=schema, unique=unique, quick=quick)
    return fut
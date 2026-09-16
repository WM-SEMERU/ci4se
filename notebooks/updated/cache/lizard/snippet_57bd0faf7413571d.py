def get_fresh(self, columns=None):
    if not columns:
        columns = ['*']
    if not self.columns:
        self.columns = columns
    return self._processor.process_select(self, self._run_select())
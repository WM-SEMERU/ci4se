def header(self):
    count = '? (error encountered)' if self._error else len(self.stats)
    utils.item('{0}: {1}'.format(self.name, count), options=self.options)
def handle(self, data):
    self.logger.debug('Handling ' + str(len(data)) + ' data items')
    for datum in data:
        if isinstance(datum, dict):
            if self._first:
                self._csv.writerow(list(datum.keys()))
                self._first = False
            self._csv.writerow(list(datum.values()))
        elif isinstance(datum, list):
            self._csv.writerow(datum)
        else:
            self.logger.warning('Ignoring unsupported data type ' + str(
                type(datum)) + ' : ' + str(datum))
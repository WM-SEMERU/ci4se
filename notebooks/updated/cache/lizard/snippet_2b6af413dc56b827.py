def write(self, s):
    for line in re.split('\\n+', s):
        if line != '':
            self._logger.log(self._level, line)
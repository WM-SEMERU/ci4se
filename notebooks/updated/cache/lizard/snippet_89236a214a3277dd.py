def write(self, text):
    index = text.find('\n')
    if index == -1:
        self._buffer = self._buffer + text
    else:
        self._buffer = self._buffer + text[:index + 1]
        if self._pattern:
            result = re.search(self._pattern, self._buffer)
            if result:
                for group in result.groups():
                    if group:
                        self._buffer = self._buffer.replace(group, '***')
        self._file.write(self._buffer)
        self._file.flush()
        self._buffer = text[index + 1:]
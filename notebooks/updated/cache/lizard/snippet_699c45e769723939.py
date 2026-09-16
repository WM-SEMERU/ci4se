def complete_func(self, findstart, base):
    self.log.debug('complete_func: in %s %s', findstart, base)

    def detect_row_column_start():
        row, col = self.editor.cursor()
        start = col
        line = self.editor.getline()
        while start > 0 and line[start - 1] not in ' .,([{':
            start -= 1
        return row, col, start if start else 1
    if str(findstart) == '1':
        row, col, startcol = detect_row_column_start()
        self.complete(row, col)
        self.completion_started = True
        return startcol
    else:
        result = []
        if self.completion_started:
            self.unqueue(timeout=self.completion_timeout, should_wait=True)
            suggestions = self.suggestions or []
            self.log.debug('complete_func: suggestions in')
            for m in suggestions:
                result.append(m)
            self.suggestions = None
            self.completion_started = False
        return result
def get_transition(self, line, line_index, column, is_escaped,
    comment_system_transitions, eof=False):
    del comment_system_transitions
    if _token_at_col_in_line(line, column, '```', 3) and not _is_escaped(line,
        column, is_escaped):
        return DisabledParser((line_index, column + 3), self.__class__,
            self._waiting_until), 3, self._started_at
    elif self._waiting_until != ParserState.EOL:
        wait_until_len = len(self._waiting_until)
        if _token_at_col_in_line(line, column, self._waiting_until,
            wait_until_len) and not _is_escaped(line, column, is_escaped):
            return InTextParser(), len(self._waiting_until), self._started_at
    elif self._waiting_until == ParserState.EOL and column == 0:
        return InTextParser(), 0, self._started_at
    elif eof:
        return InTextParser(), 0, self._started_at
    return self, 1, None
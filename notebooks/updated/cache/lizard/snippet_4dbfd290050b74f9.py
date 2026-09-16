def _get_next_line_indent_delta(self, newline_token):
    assert newline_token.type == 'NEWLINE', 'Can only search for a dent starting from a newline.'
    next_line_pos = newline_token.lexpos + len(newline_token.value)
    if next_line_pos == len(newline_token.lexer.lexdata):
        return None
    line = newline_token.lexer.lexdata[next_line_pos:].split(os.linesep, 1)[0]
    if not line:
        return None
    lstripped_line = line.lstrip()
    lstripped_line_length = len(lstripped_line)
    if lstripped_line_length == 0:
        return None
    if lstripped_line[0] == '#':
        return None
    indent = len(line) - lstripped_line_length
    if indent % 4 > 0:
        self.errors.append(('Indent is not divisible by 4.', newline_token.
            lexer.lineno))
        return None
    indent_delta = indent - _indent_level_to_spaces_count(self.cur_indent)
    return indent_delta // 4
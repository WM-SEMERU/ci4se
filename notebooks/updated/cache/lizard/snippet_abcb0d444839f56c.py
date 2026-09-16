def parse_py_statement(line):
    state = 0
    cur_token = ''
    spaces = ' \t\n'
    ops = '.,;:+-*/%&!=|(){}[]^<>'
    i = 0

    def _escape_char(_c):
        if _c == 'n':
            return '\n'
        elif _c == 't':
            return '\t'
        else:
            return _c
    while i < len(line):
        c = line[i]
        i += 1
        if state == 0:
            if c in spaces:
                pass
            elif c in ops:
                yield 'op', c
            elif c == '#':
                state = 6
            elif c == '"':
                state = 1
            elif c == "'":
                state = 2
            else:
                cur_token = c
                state = 3
        elif state == 1:
            if c == '\\':
                state = 4
            elif c == '"':
                yield 'str', cur_token
                cur_token = ''
                state = 0
            else:
                cur_token += c
        elif state == 2:
            if c == '\\':
                state = 5
            elif c == "'":
                yield 'str', cur_token
                cur_token = ''
                state = 0
            else:
                cur_token += c
        elif state == 3:
            if c in spaces + ops + '#"\'':
                yield 'id', cur_token
                cur_token = ''
                state = 0
                i -= 1
            else:
                cur_token += c
        elif state == 4:
            cur_token += _escape_char(c)
            state = 1
        elif state == 5:
            cur_token += _escape_char(c)
            state = 2
        elif state == 6:
            cur_token += c
    if state == 3:
        yield 'id', cur_token
    elif state == 6:
        yield 'comment', cur_token
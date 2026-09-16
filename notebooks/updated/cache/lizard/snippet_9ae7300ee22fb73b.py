def log_trace(self, tag, original, loc, tokens=None, extra=None):
    if self.tracing:
        tag, original, loc = displayable(tag), displayable(original), int(loc)
        if '{' not in tag:
            out = ['[' + tag + ']']
            add_line_col = True
            if tokens is not None:
                if isinstance(tokens, Exception):
                    msg = displayable(str(tokens))
                    if '{' in msg:
                        head, middle = msg.split('{', 1)
                        middle, tail = middle.rsplit('}', 1)
                        msg = head + '{...}' + tail
                    out.append(msg)
                    add_line_col = False
                elif len(tokens) == 1 and isinstance(tokens[0], str):
                    out.append(ascii(tokens[0]))
                else:
                    out.append(ascii(tokens))
            if add_line_col:
                out.append('(line:' + str(lineno(loc, original)) + ', col:' +
                    str(col(loc, original)) + ')')
            if extra is not None:
                out.append('from ' + ascii(extra))
            printerr(*out)
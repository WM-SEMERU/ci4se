def str_repl(self, inputstring, **kwargs):
    out = []
    comment = None
    string = None
    for i, c in enumerate(append_it(inputstring, None)):
        try:
            if comment is not None:
                if c is not None and c in nums:
                    comment += c
                elif c == unwrapper and comment:
                    ref = self.get_ref('comment', comment)
                    if out and not out[-1].endswith('\n'):
                        out[-1] = out[-1].rstrip(' ')
                        if not self.minify:
                            out[-1] += '  '
                    out.append('#' + ref)
                    comment = None
                else:
                    raise CoconutInternalException('invalid comment marker in',
                        getline(i, inputstring))
            elif string is not None:
                if c is not None and c in nums:
                    string += c
                elif c == unwrapper and string:
                    text, strchar = self.get_ref('str', string)
                    out.append(strchar + text + strchar)
                    string = None
                else:
                    raise CoconutInternalException('invalid string marker in',
                        getline(i, inputstring))
            elif c is not None:
                if c == '#':
                    comment = ''
                elif c == strwrapper:
                    string = ''
                else:
                    out.append(c)
        except CoconutInternalException as err:
            complain(err)
            if comment is not None:
                out.append(comment)
                comment = None
            if string is not None:
                out.append(string)
                string = None
            out.append(c)
    return ''.join(out)
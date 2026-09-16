def structure(self):

    def _rstrip_backslash(l):
        l = l.rstrip()
        if l.endswith('\\'):
            return l[:-1]
        return l
    instructions = []
    lineno = -1
    insnre = re.compile('^\\s*(\\w+)\\s+(.*)$')
    contre = re.compile('^.*\\\\\\s*$')
    commentre = re.compile('^\\s*#')
    in_continuation = False
    current_instruction = None
    for line in self.lines:
        lineno += 1
        if commentre.match(line):
            continue
        if not in_continuation:
            m = insnre.match(line)
            if not m:
                continue
            current_instruction = {'instruction': m.groups()[0].upper(),
                'startline': lineno, 'endline': lineno, 'content': line,
                'value': _rstrip_backslash(m.groups()[1])}
        else:
            current_instruction['content'] += line
            current_instruction['endline'] = lineno
            if current_instruction['value']:
                current_instruction['value'] += _rstrip_backslash(line)
            else:
                current_instruction['value'] = _rstrip_backslash(line.lstrip())
        in_continuation = contre.match(line)
        if not in_continuation and current_instruction is not None:
            instructions.append(current_instruction)
    return instructions
def push(self, line):
    if transforms.FROM_EXPERIMENTAL.match(line):
        transforms.add_transformers(line)
        self.buffer.append('\n')
    else:
        self.buffer.append(line)
    add_pass = False
    if line.rstrip(' ').endswith(':'):
        add_pass = True
    source = '\n'.join(self.buffer)
    if add_pass:
        source += 'pass'
    source = transforms.transform(source)
    if add_pass:
        source = source.rstrip(' ')
        if source.endswith('pass'):
            source = source[:-4]
    if not self.buffer[-1]:
        source += '\n'
    try:
        more = self.runsource(source, self.filename)
    except SystemExit:
        os._exit(1)
    if not more:
        self.resetbuffer()
    return more
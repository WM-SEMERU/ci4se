def fix_chain_id(self):
    for i in xrange(len(self.lines)):
        line = self.lines[i]
        if line.startswith('ATOM') and line[21] == ' ':
            self.lines[i] = line[:21] + 'A' + line[22:]
def on_print(self, node):
    dest = self.run(node.dest) or self.writer
    end = ''
    if node.nl:
        end = '\n'
    out = [self.run(tnode) for tnode in node.values]
    if out and len(self.error) == 0:
        self._printer(*out, file=dest, end=end)
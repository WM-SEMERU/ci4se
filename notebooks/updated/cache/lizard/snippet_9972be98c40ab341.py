def marker_for_line(self, line):
    block = self.editor.document().findBlockByNumber(line)
    try:
        return block.userData().messages
    except AttributeError:
        return []
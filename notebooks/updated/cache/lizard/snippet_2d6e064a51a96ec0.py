def mapToAbsPosition(self, line, column):
    block = self.document().findBlockByNumber(line)
    if not block.isValid():
        raise IndexError('Invalid line index %d' % line)
    if column >= block.length():
        raise IndexError('Invalid column index %d' % column)
    return block.position() + column
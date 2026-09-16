def _findExpressionEnd(self, block):
    while block.isValid():
        column = self._lastColumn(block)
        if column > 0:
            return block, column
        block = block.previous()
    raise UserWarning()
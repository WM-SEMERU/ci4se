def _makeIndentAsColumn(self, block, column, offset=0):
    blockText = block.text()
    textBeforeColumn = blockText[:column]
    tabCount = textBeforeColumn.count('\t')
    visibleColumn = column + tabCount * (self._indenter.width - 1)
    return self._makeIndentFromWidth(visibleColumn + offset)
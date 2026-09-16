def tryCComment(self, block):
    indentation = None
    prevNonEmptyBlock = self._prevNonEmptyBlock(block)
    if not prevNonEmptyBlock.isValid():
        return None
    prevNonEmptyBlockText = prevNonEmptyBlock.text()
    if prevNonEmptyBlockText.endswith('*/'):
        try:
            foundBlock, notUsedColumn = self.findTextBackward(prevNonEmptyBlock
                , prevNonEmptyBlock.length(), '/*')
        except ValueError:
            foundBlock = None
        if foundBlock is not None:
            dbg('tryCComment: success (1) in line %d' % foundBlock.
                blockNumber())
            return self._lineIndent(foundBlock.text())
    if prevNonEmptyBlock != block.previous():
        return None
    blockTextStripped = block.text().strip()
    prevBlockTextStripped = prevNonEmptyBlockText.strip()
    if prevBlockTextStripped.startswith('/*'
        ) and not '*/' in prevBlockTextStripped:
        indentation = self._blockIndent(prevNonEmptyBlock)
        if CFG_AUTO_INSERT_STAR:
            indentation += ' '
            if not blockTextStripped.endswith('*'):
                indentation += '*'
            secondCharIsSpace = len(blockTextStripped
                ) > 1 and blockTextStripped[1].isspace()
            if not secondCharIsSpace and not blockTextStripped.endswith('*/'):
                indentation += ' '
        dbg('tryCComment: success (2) in line %d' % block.blockNumber())
        return indentation
    elif prevBlockTextStripped.startswith('*') and (len(
        prevBlockTextStripped) == 1 or prevBlockTextStripped[1].isspace()):
        indentation = self._lineIndent(prevNonEmptyBlockText)
        if CFG_AUTO_INSERT_STAR and not blockTextStripped.startswith('*'):
            indentation += '*'
            if len(blockTextStripped) < 2 or not blockTextStripped[1].isspace(
                ):
                indentation += ' '
        dbg('tryCComment: success (2) in line %d' % block.blockNumber())
        return indentation
    return None
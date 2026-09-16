def trySwitchStatement(self, block):
    if not re.match('^\\s*(default\\s*|case\\b.*):', block.text()):
        return None
    for block in self.iterateBlocksBackFrom(block.previous()):
        text = block.text()
        if re.match('^\\s*(default\\s*|case\\b.*):', text):
            dbg('trySwitchStatement: success in line %d' % block.blockNumber())
            return self._lineIndent(text)
        elif re.match('^\\s*switch\\b', text):
            if CFG_INDENT_CASE:
                return self._increaseIndent(self._lineIndent(text))
            else:
                return self._lineIndent(text)
    return None
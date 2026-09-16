def _parseXpathScope(self):
    rd = self.refsDecl
    matches = REFSDECL_SPLITTER.findall(rd)
    return REFSDECL_REPLACER.sub('?', ''.join(matches[0:-1])
        ), REFSDECL_REPLACER.sub('?', matches[-1])
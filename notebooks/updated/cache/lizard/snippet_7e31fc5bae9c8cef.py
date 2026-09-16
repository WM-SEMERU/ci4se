def _parseRuleset(self, src):
    src, selectors = self._parseSelectorGroup(src)
    src, properties = self._parseDeclarationGroup(src.lstrip())
    result = self.cssBuilder.ruleset(selectors, properties)
    return src, result
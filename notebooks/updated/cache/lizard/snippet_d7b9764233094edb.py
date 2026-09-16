def fill(self, passage=None, xpath=None):
    if xpath is True:
        xpath = self.xpath
        replacement = '\\1'
        if isinstance(passage, str):
            replacement = "\\1\\2'" + passage + "'"
        return REFERENCE_REPLACER.sub(replacement, xpath)
    else:
        if isinstance(passage, CtsReference):
            passage = passage.start.list
        elif passage is None:
            return REFERENCE_REPLACER.sub('\\1', self.refsDecl)
        passage = iter(passage)
        return REFERENCE_REPLACER.sub(lambda m: _ref_replacer(m, passage),
            self.refsDecl)
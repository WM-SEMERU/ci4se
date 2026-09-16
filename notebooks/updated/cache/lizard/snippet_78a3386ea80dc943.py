def _get_synonym(self, line):
    mtch = self.attr2cmp['synonym'].match(line)
    text, scope, typename, dbxrefs, _ = mtch.groups()
    typename = typename.strip()
    dbxrefs = set(dbxrefs.split(', ')) if dbxrefs else set()
    return self.attr2cmp['synonym nt']._make([text, scope, typename, dbxrefs])
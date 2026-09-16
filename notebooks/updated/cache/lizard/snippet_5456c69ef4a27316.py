def _rt_parse_execs(self, statement, element, mode, lineparser):
    if mode == 'insert':
        enew, start, end = self.xparser.parse_signature(statement, element,
            element)
        if enew is not None:
            enew.start, enew.end = lineparser.absolute_charindex(statement,
                start, end)
            enew.incomplete = True
            element.executables[enew.name.lower()] = enew
            lineparser.additions.append((enew, element))
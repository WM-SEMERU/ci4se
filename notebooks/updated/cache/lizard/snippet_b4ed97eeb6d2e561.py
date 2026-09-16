def lines(self):
    if self.name != 'Root':
        yield 'Section', '|'.join([self.value] + self.property_names)
    for row in self.rows:
        term, value = row
        if not isinstance(value, (list, tuple)):
            value = [value]
        term = term.replace('root.', '').title()
        yield term, value[0]
        children = list(zip(self.property_names, value[1:]))
        for prop, value in children:
            if value and value.strip():
                child_t = '.' + prop.title()
                yield '    ' + child_t, value
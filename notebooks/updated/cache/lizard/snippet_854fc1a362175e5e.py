def definition(self, text, definition):
    text = text.strip()
    definition = definition.strip()
    regex = re.compile('\\n(\\S)')
    definition = regex.sub('\n    \\g<1>', definition)
    return '%(text)s\n:    %(definition)s' % locals()
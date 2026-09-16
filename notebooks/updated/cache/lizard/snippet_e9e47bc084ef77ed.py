def parse_file(self, sg_file=None, data=None):
    if sg_file is not None and data is not None:
        raise ArgumentError(
            'You must pass either a path to an sgf file or the sgf contents but not both'
            )
    if sg_file is None and data is None:
        raise ArgumentError(
            'You must pass either a path to an sgf file or the sgf contents, neither passed'
            )
    if sg_file is not None:
        try:
            with open(sg_file, 'r') as inf:
                data = inf.read()
        except IOError:
            raise ArgumentError('Could not read sensor graph file', path=
                sg_file)
    data = data.replace('\t', '    ')
    lang = get_language()
    result = lang.parseString(data)
    for statement in result:
        parsed = self.parse_statement(statement, orig_contents=data)
        self.statements.append(parsed)
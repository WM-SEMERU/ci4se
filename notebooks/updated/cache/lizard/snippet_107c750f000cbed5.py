def from_statement(cls, statement, filename='<expr>'):
    lines = textwrap.dedent(statement).split('\n')
    if lines and not lines[0]:
        lines = lines[1:]
    blob = '\n'.join(lines).encode('utf-8')
    tree = cls._parse(blob, filename)
    return cls(blob=blob, tree=tree, root=None, filename=filename)
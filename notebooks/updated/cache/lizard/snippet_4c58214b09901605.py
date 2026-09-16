def attrgetter_atom_split(tokens):
    if len(tokens) == 1:
        return tokens[0], None
    elif len(tokens) >= 2 and tokens[1] == '(':
        if len(tokens) == 2:
            return tokens[0], ''
        elif len(tokens) == 3:
            return tokens[0], tokens[2]
        else:
            raise CoconutInternalException(
                'invalid methodcaller literal tokens', tokens)
    else:
        raise CoconutInternalException('invalid attrgetter literal tokens',
            tokens)
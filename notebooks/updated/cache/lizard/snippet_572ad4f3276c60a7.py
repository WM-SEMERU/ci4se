def _tokenize_by_character_class(s):
    character_classes = [string.digits, string.ascii_letters, string.
        punctuation, string.whitespace]
    result = []
    rest = list(s)
    while rest:
        progress = False
        for character_class in character_classes:
            if rest[0] in character_class:
                progress = True
                token = ''
                for take_away in itertools.takewhile(lambda c: c in
                    character_class, rest[:]):
                    token += take_away
                    rest.pop(0)
                result.append(token)
                break
        if not progress:
            result.append(rest[0])
            rest = rest[1:]
    return result
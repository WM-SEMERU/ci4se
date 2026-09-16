def all_matches(grammar, text):
    for tokens, start, stop in grammar.parseWithTabs().scanString(text):
        yield unpack(tokens), start, stop
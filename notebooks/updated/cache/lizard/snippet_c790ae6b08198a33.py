def to_type(self, tokens):
    result = []
    name_tokens = []
    reference = pointer = array = False
    inside_array = False
    empty_array = True
    templated_tokens = []

    def add_type():
        if not name_tokens:
            return
        names = []
        modifiers = []
        for t in name_tokens:
            if keywords.is_keyword(t.name):
                modifiers.append(t.name)
            else:
                names.append(t.name)
        name = ''.join(names)
        templated_types = self.to_type(templated_tokens)
        result.append(Type(name_tokens[0].start, name_tokens[-1].end, name,
            templated_types, modifiers, reference, pointer, array))
        del name_tokens[:]
        del templated_tokens[:]
    i = 0
    end = len(tokens)
    while i < end:
        token = tokens[i]
        if token.name == ']':
            inside_array = False
            if empty_array:
                pointer = True
            else:
                array = True
        elif inside_array:
            empty_array = False
        elif token.name == '<':
            templated_tokens, i = self._get_template_end(tokens, i + 1)
            continue
        elif token.name == ',' or token.name == '(':
            add_type()
            reference = pointer = array = False
            empty_array = True
        elif token.name == '*':
            pointer = True
        elif token.name == '&':
            reference = True
        elif token.name == '[':
            inside_array = True
        elif token.name != ')':
            name_tokens.append(token)
        i += 1
    add_type()
    return result
def json_token_to_estner_token(json_token):
    token = Token()
    word = json_token[TEXT]
    lemma = word
    morph = ''
    label = 'O'
    ending = json_token[ENDING]
    root_toks = json_token[ROOT_TOKENS]
    if isinstance(root_toks[0], list):
        root_toks = root_toks[0]
    lemma = '_'.join(root_toks) + ('+' + ending if ending else '')
    if not lemma:
        lemma = word
    morph = '_%s_' % json_token[POSTAG]
    morph += ' ' + json_token[FORM]
    if LABEL in json_token:
        label = json_token[LABEL]
    return Token(word, lemma, morph, label)
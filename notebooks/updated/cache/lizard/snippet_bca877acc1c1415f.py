def _matchremove_verb_endings(self, word):
    i_verb_endings = ['iuntur', 'erunt', 'untur', 'iunt', 'unt']
    bi_verb_endings = ['beris', 'bor', 'bo']
    eri_verb_endings = ['ero']
    verb_endings = ['mini', 'ntur', 'stis', 'mur', 'mus', 'ris', 'sti',
        'tis', 'tur', 'ns', 'nt', 'ri', 'm', 'r', 's', 't']
    for ending in i_verb_endings:
        if word.endswith(ending):
            word = re.sub('{0}$'.format(ending), 'i', word)
            return word
    for ending in bi_verb_endings:
        if word.endswith(ending):
            word = re.sub('{0}$'.format(ending), 'bi', word)
            return word
    for ending in eri_verb_endings:
        if word.endswith(ending):
            word = re.sub('{0}$'.format(ending), 'eri', word)
            return word
    for ending in verb_endings:
        if word.endswith(ending):
            word = re.sub('{0}$'.format(ending), '', word)
            break
    return word
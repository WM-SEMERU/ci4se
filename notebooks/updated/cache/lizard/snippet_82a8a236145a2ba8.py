def _words_at_the_beginning(word, tree, prefix=''):
    l = []
    if '' in tree:
        l.append([prefix, tree['']])
    if len(word) > 0 and word[0] in tree:
        l.extend(_words_at_the_beginning(word[1:], tree[word[0]], prefix=
            prefix + word[0]))
    return l
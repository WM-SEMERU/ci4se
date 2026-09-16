def corenlp_to_xmltree(s, prune_root=True):
    s = get_as_dict(s)
    if not ('dep_parents' in s and isinstance(s['dep_parents'], list)):
        raise ValueError(
            "Input CoreNLP object must have a 'dep_parents' attribute which is a list"
            )
    try:
        dep_parents = list(map(int, s['dep_parents']))
    except Exception:
        raise ValueError("'dep_parents' attribute must be a list of ints")
    b = min(dep_parents)
    if b != 0:
        dep_parents = list(map(lambda j: j - b, dep_parents))
    root = corenlp_to_xmltree_sub(s, dep_parents, 0)
    if prune_root:
        for c in root:
            if len(c) == 0:
                root.remove(c)
        if len(root) == 1:
            root = root.findall('./*')[0]
    return XMLTree(root, words=s['words'])
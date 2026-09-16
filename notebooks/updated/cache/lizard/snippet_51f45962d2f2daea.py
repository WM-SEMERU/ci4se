def fuzzy_match_tipnames(ttree, names, wildcard, regex, mrca=True, mono=True):
    if not any([names, wildcard, regex]):
        raise ToytreeError(
            'must enter an outgroup, wildcard selector, or regex pattern')
    tips = []
    if names:
        if isinstance(names, (str, int)):
            names = [names]
        notfound = [i for i in names if i not in ttree.get_tip_labels()]
        if any(notfound):
            raise ToytreeError('Sample {} is not in the tree'.format(notfound))
        tips = [i for i in ttree.treenode.get_leaves() if i.name in names]
    elif regex:
        tips = [i for i in ttree.treenode.get_leaves() if re.match(regex, i
            .name)]
        if not any(tips):
            raise ToytreeError('No Samples matched the regular expression')
    elif wildcard:
        tips = [i for i in ttree.treenode.get_leaves() if wildcard in i.name]
        if not any(tips):
            raise ToytreeError('No Samples matched the wildcard')
    if not tips:
        raise ToytreeError('no matching tipnames')
    tipnames = [i.name for i in tips]
    if len(tips) == 1:
        if mrca:
            return tips[0]
        else:
            return tipnames
    mbool, mtype, mnames = ttree.treenode.check_monophyly(tipnames, 'name',
        ignore_missing=True)
    node = ttree.treenode.get_common_ancestor(tips)
    if mono:
        if not mbool:
            raise ToytreeError('Taxon list cannot be paraphyletic')
    if not mrca:
        return tipnames
    else:
        return node
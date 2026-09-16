def get_group_tokens(root):
    global all_markers
    if root in all_markers or root in ['-', '_']:
        return [[root]]
    groups = []
    for group in root.split('-'):
        toks = [trim_phonetics(trim_compounds(tok)) for tok in group.split('_')
            ]
        groups.append(toks)
    return groups
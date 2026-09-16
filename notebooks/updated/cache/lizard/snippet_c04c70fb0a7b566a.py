def uproot(tree):
    uprooted = tree.copy()
    uprooted.parent = None
    for child in tree.all_children():
        uprooted.add_general_child(child)
    return uprooted
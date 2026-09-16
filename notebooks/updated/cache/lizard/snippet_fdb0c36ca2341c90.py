def get_root(root, phonetic, compound):
    global compound_regex
    if not phonetic:
        root = trim_phonetics(root)
    if not compound:
        root = trim_compounds(root)
    return root
def trim_phonetics(root):
    global phonetic_markers
    global phonetic_regex
    if root in phonetic_markers:
        return root
    else:
        return phonetic_regex.sub('', root)
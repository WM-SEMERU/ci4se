def category_replace(text, replacements=UNICODE_CATEGORIES):
    if text is None:
        return None
    characters = []
    for character in decompose_nfkd(text):
        cat = category(character)
        replacement = replacements.get(cat, character)
        if replacement is not None:
            characters.append(replacement)
    return ''.join(characters)
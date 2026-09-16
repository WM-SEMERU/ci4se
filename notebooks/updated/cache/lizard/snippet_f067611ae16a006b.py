def tmpl_replchars(text, replace, chars):
    for char in chars:
        text = text.replace(char, replace)
    return text
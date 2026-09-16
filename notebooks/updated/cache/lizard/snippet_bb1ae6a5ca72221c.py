def colored_map(text, cmap):
    if not __ISON:
        return text
    for key, v in cmap.items():
        if isinstance(v, dict):
            text = text.replace(key, colored(key, **v))
        else:
            text = text.replace(key, colored(key, color=v))
    return text
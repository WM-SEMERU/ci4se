def remove_suffix(text, suffix):
    rest, suffix, null = text.partition(suffix)
    return rest
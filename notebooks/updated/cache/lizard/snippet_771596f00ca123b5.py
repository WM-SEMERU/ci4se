def tree_attribute(identifier):
    if identifier[0].upper().isupper() is False and identifier[0] != '_':
        return True
    else:
        return identifier[0].isupper()
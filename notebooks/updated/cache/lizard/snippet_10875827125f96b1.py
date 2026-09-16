def fully_qualify_alias_labels(label, aliases):
    for alias, full_name in aliases.items():
        if label == alias:
            return full_name
        elif label.startswith(alias + '.'):
            return full_name + label[len(alias):]
    return label
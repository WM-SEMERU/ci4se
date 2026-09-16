def color_key(tkey):
    name = tkey.GetName()
    classname = tkey.GetClassName()
    for class_regex, color in _COLOR_MATCHER:
        if class_regex.match(classname):
            return colored(name, color=color)
    return name
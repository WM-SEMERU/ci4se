def hwpack_names():
    ls = hwpack_dir().listdir()
    ls = [x.name for x in ls]
    ls = [x for x in ls if x != 'tools']
    arduino_included = 'arduino' in ls
    ls = [x for x in ls if x != 'arduino']
    ls.sort()
    if arduino_included:
        ls = ['arduino'] + ls
    return ls
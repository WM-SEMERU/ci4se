def name(self):
    name = self.__class__.__name__
    for i, character in enumerate(name):
        if character.isdigit():
            return name[:i] + '-' + name[i:]
    return name
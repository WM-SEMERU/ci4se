def suffix(self):
    name = self.name
    i = name.rfind('.')
    if 0 < i < len(name) - 1:
        return name[i:]
    else:
        return ''
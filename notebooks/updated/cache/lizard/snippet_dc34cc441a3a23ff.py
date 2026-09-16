def match(self, obj):
    path, frag = [], obj
    for part in self.parts:
        path.append(part)
        if isinstance(frag, dict):
            try:
                frag = frag[part]
            except KeyError:
                return False
        elif isinstance(frag, (list, tuple)):
            frag = part in frag
        elif isinstance(frag, str):
            frag = frag == part
        elif isinstance(frag, int):
            frag = frag == int(part)
        else:
            return False
    return True if frag else False
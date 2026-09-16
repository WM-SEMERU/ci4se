def css(src, dest=False, shift=4):
    if not dest:
        return _css(_text(src))
    elif type(dest) is int:
        return _css(_text(src), dest)
    else:
        with open(dest, 'w') as f2:
            return f2.write(_css(_text(src), shift))
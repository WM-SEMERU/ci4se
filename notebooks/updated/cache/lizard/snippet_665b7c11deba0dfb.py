def parse(cls, fptr, offset, length):
    box = cls(length=length, offset=offset)
    box.box = box.parse_superbox(fptr)
    return box
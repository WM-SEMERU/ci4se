def from_string(cls, width, height, rgba_string):
    raw = ''
    for i in range(0, len(rgba_string), 4):
        raw += rgba_string[i + 3]
        raw += rgba_string[i:i + 3]
    assert len(rgba_string) == width * height * 4
    return Form(width=width, height=height, depth=32, bits=Bitmap(raw))
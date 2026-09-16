def __read_byte_size(decl, attrs):
    size = attrs.get(XML_AN_SIZE, 0)
    decl.byte_size = int(size) / 8
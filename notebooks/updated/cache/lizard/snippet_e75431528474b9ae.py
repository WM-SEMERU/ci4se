def read_ds9(filename, errors='strict'):
    with open(filename) as fh:
        region_string = fh.read()
    parser = DS9Parser(region_string, errors=errors)
    return parser.shapes.to_regions()
def read_interoperability_ifd(fh, byteorder, dtype, count, offsetsize):
    tag_names = {(1): 'InteroperabilityIndex'}
    return read_tags(fh, byteorder, offsetsize, tag_names, maxifds=1)
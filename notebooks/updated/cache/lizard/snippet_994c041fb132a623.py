def dst_to_src(self, dst_file):
    for map in self.mappings:
        src_uri = map.dst_to_src(dst_file)
        if src_uri is not None:
            return src_uri
    raise MapperError(
        'Unable to translate destination path (%s) into a source URI.' %
        dst_file)
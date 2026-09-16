def from_offset(tu, file, offset):
    return conf.lib.clang_getLocationForOffset(tu, file, offset)
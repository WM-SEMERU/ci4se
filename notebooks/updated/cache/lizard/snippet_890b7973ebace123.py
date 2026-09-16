def _unpack_version(tag_data):
    tag = tag_data & (1 << 20) - 1
    version_data = tag_data >> 20
    major = version_data >> 6 & (1 << 6) - 1
    minor = version_data >> 0 & (1 << 6) - 1
    return tag, '{}.{}'.format(major, minor)
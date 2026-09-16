def geometry_hash(geometry):
    if hasattr(geometry, 'md5'):
        md5 = geometry.md5()
    elif hasattr(geometry, 'tostring'):
        md5 = str(hash(geometry.tostring()))
    if hasattr(geometry, 'visual'):
        md5 += str(geometry.visual.crc())
    return md5
def write_cache(entries, stream, extension_data=None, ShaStreamCls=
    IndexFileSHA1Writer):
    stream = ShaStreamCls(stream)
    tell = stream.tell
    write = stream.write
    version = 2
    write(b'DIRC')
    write(pack('>LL', version, len(entries)))
    for entry in entries:
        beginoffset = tell()
        write(entry[4])
        write(entry[5])
        path = entry[3]
        path = force_bytes(path, encoding=defenc)
        plen = len(path) & CE_NAMEMASK
        assert plen == len(path), 'Path %s too long to fit into index' % entry[
            3]
        flags = plen | entry[2] & CE_NAMEMASK_INV
        write(pack('>LLLLLL20sH', entry[6], entry[7], entry[0], entry[8],
            entry[9], entry[10], entry[1], flags))
        write(path)
        real_size = tell() - beginoffset + 8 & ~7
        write(b'\x00' * (beginoffset + real_size - tell()))
    if extension_data is not None:
        stream.write(extension_data)
    stream.write_sha()
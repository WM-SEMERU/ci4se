def write_chunk(outfile, tag, data=b''):
    data = bytes(data)
    outfile.write(struct.pack('!I', len(data)))
    outfile.write(tag)
    outfile.write(data)
    checksum = zlib.crc32(tag)
    checksum = zlib.crc32(data, checksum)
    checksum &= 2 ** 32 - 1
    outfile.write(struct.pack('!I', checksum))
def String(self, off):
    N.enforce_number(off, N.UOffsetTFlags)
    off += encode.Get(N.UOffsetTFlags.packer_type, self.Bytes, off)
    start = off + N.UOffsetTFlags.bytewidth
    length = encode.Get(N.UOffsetTFlags.packer_type, self.Bytes, off)
    return bytes(self.Bytes[start:start + length])
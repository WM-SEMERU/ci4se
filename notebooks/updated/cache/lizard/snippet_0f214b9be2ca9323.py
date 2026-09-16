def readBinary(self, filename=None):
    if filename is None:
        filename = self.pathname
    stream = open(filename, 'rb')
    magic = struct.unpack('>H', stream.read(2))[0]
    self.crc32 = struct.unpack('>I', stream.read(4))[0]
    self.seqid = struct.unpack('>H', stream.read(2))[0]
    self.version = struct.unpack('>H', stream.read(2))[0]
    ncmds = struct.unpack('>H', stream.read(2))[0]
    reserved = stream.read(20)
    for n in range(ncmds):
        bytes = stream.read(110)
        self.lines.append(SeqCmd.decode(bytes, self.cmddict))
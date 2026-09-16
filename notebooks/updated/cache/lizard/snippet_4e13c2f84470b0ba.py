def wave_infochunk(path):
    with open(path, 'rb') as file:
        if file.read(4) != b'RIFF':
            return None
        data_size = file.read(4)
        if file.read(4) != b'WAVE':
            return None
        while True:
            chunkid = file.read(4)
            sizebuf = file.read(4)
            if len(sizebuf) < 4 or len(chunkid) < 4:
                return None
            size = struct.unpack(b'<L', sizebuf)[0]
            if chunkid[0:3] != b'fmt':
                if size % 2 == 1:
                    seek = size + 1
                else:
                    seek = size
                file.seek(size, 1)
            else:
                return bytearray(b'RIFF' + data_size + b'WAVE' + chunkid +
                    sizebuf + file.read(size))
def append(self, box):
    if self._codec_format == opj2.CODEC_J2K:
        msg = 'Only JP2 files can currently have boxes appended to them.'
        raise IOError(msg)
    if not (box.box_id == 'xml ' or box.box_id == 'uuid' and box.uuid ==
        UUID('be7acfcb-97a9-42e8-9c71-999491e3afac')):
        msg = 'Only XML boxes and XMP UUID boxes can currently be appended.'
        raise IOError(msg)
    with open(self.filename, 'rb') as ifile:
        offset = self.box[-1].offset
        ifile.seek(offset)
        read_buffer = ifile.read(4)
        box_length, = struct.unpack('>I', read_buffer)
        if box_length == 0:
            true_box_length = os.path.getsize(ifile.name) - offset
            with open(self.filename, 'r+b') as ofile:
                ofile.seek(offset)
                write_buffer = struct.pack('>I', true_box_length)
                ofile.write(write_buffer)
    with open(self.filename, 'ab') as ofile:
        box.write(ofile)
    self.parse()
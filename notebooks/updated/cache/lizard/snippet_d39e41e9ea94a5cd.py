def determine_packet_positions(self):
    print('Analysing file...')
    self.rewind_file()
    with ignored(struct.error):
        while True:
            pointer_position = self.blob_file.tell()
            length = struct.unpack('<i', self.blob_file.read(4))[0]
            self.packet_positions.append(pointer_position)
            self.blob_file.seek(length, 1)
    self.rewind_file()
    print('Found {0} CLB UDP packets.'.format(len(self.packet_positions)))
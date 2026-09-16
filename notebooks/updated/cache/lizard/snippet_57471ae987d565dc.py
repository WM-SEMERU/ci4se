def browse(self):
    offset = 0
    for record in self.reader:
        record.payload = StringIO(record.payload.read(1024 * 1024))
        self.reader.finish_reading_current_record()
        next_offset = self.tell()
        yield record, offset, next_offset - offset
        offset = next_offset
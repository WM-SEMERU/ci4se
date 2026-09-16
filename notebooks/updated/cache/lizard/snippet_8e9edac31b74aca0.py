def iter_rows(self):
    fileobj = self._fileobj
    cls_row = self.cls_row
    fields = self.fields
    for idx in range(self.prolog.records_count):
        data = fileobj.read(1)
        marker = struct.unpack('<1s', data)[0]
        is_deleted = marker == b'*'
        if is_deleted:
            continue
        row_values = []
        for field in fields:
            val = field.cast(fileobj.read(field.len))
            row_values.append(val)
        yield cls_row(*row_values)
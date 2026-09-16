def _make_record(self, parent, gline):
    if parent and gline.tag in ('CONT', 'CONC'):
        if parent.tag != 'BLOB':
            value = gline.value
            if gline.tag == 'CONT':
                value = b'\n' + (value or b'')
            if value is not None:
                parent.value = (parent.value or b'') + value
        return None
    dialect = model.DIALECT_DEFAULT
    if not (gline.level == 0 and gline.tag == 'HEAD') and self._header:
        dialect = self.dialect
    rec = model.make_record(level=gline.level, xref_id=gline.xref_id, tag=
        gline.tag, value=gline.value, sub_records=[], offset=gline.offset,
        dialect=dialect, parser=self)
    if parent:
        parent.sub_records.append(rec)
    return rec
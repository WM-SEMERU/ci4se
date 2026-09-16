def _merge_chunks(self):
    if not self._indefinite:
        return self._as_chunk()
    pointer = self._chunks_offset
    contents_len = len(self.contents)
    output = None
    while pointer < contents_len:
        sub_value, pointer = _parse_build(self.contents, pointer, spec=self
            .__class__)
        if output is None:
            output = sub_value._merge_chunks()
        else:
            output += sub_value._merge_chunks()
    if output is None:
        return self._as_chunk()
    return output
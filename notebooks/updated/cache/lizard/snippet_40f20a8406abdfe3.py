def preprocess(self):
    tokens = self.tokenize()
    pl_segments, has_perl_tags = self.get_perl_segments(tokens)
    str_parts = []
    smap = segment_map.SegmentMap()
    offset = 0
    if has_perl_tags:
        emit_list = self.run_perl_miniscript(pl_segments)
        for entry in emit_list:
            if entry['type'] == 'ref':
                pl_seg = pl_segments[entry['ref']]
                emit_text = pl_seg.get_text()
                map_seg = segment_map.UnalteredSegment(offset, offset + len
                    (emit_text) - 1, pl_seg.start, pl_seg.end, pl_seg.
                    file_pp.path, pl_seg.file_pp.incl_ref)
                offset += len(emit_text)
                smap.segments.append(map_seg)
                str_parts.append(emit_text)
            elif entry['type'] == 'text':
                pl_seg = pl_segments[entry['ref']]
                emit_text = entry['text']
                map_seg = segment_map.MacroSegment(offset, offset + len(
                    emit_text) - 1, pl_seg.start, pl_seg.end, pl_seg.
                    file_pp.path, pl_seg.file_pp.incl_ref)
                offset += len(emit_text)
                smap.segments.append(map_seg)
                str_parts.append(emit_text)
    else:
        for pl_seg in pl_segments:
            emit_text = pl_seg.get_text()
            map_seg = segment_map.UnalteredSegment(offset, offset + len(
                emit_text) - 1, pl_seg.start, pl_seg.end, pl_seg.file_pp.
                path, pl_seg.file_pp.incl_ref)
            offset += len(emit_text)
            smap.segments.append(map_seg)
            str_parts.append(emit_text)
    return ''.join(str_parts), smap
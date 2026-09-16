def get_perl_segments(self, tokens):
    pl_segments = []
    has_perl_tags = False
    pos = 0
    for typ, start, end in tokens:
        if start != pos:
            pl_seg = PPPUnalteredSegment(self, pos, start - 1)
            pl_segments.append(pl_seg)
        if typ == 'incl':
            end, incl_path = self.parse_include(start)
            incl_ref = segment_map.IncludeRef(start, end, self.path, self.
                incl_ref)
            incl_file_pp = FilePreprocessor(self.env, incl_path, self.
                search_paths, incl_ref)
            incl_tokens = incl_file_pp.tokenize()
            incl_pl_segments, incl_has_pl_tags = (incl_file_pp.
                get_perl_segments(incl_tokens))
            pl_segments.extend(incl_pl_segments)
            has_perl_tags = has_perl_tags or incl_has_pl_tags
        else:
            if self.text[start + 2] == '=':
                pl_seg = PPPMacroSegment(self, start, end)
            else:
                pl_seg = PPPPerlSegment(self, start, end)
            pl_segments.append(pl_seg)
            has_perl_tags = True
        pos = end + 1
    text_len = len(self.text)
    if text_len > pos:
        pl_seg = PPPUnalteredSegment(self, pos, text_len - 1)
        pl_segments.append(pl_seg)
    return pl_segments, has_perl_tags
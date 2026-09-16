def process_strings(self, string, docstrings=False):
    m = RE_STRING_TYPE.match(string)
    stype = self.get_string_type(m.group(1) if m.group(1) else '')
    if not self.match_string(stype) and not docstrings:
        return '', False
    is_bytes = 'b' in stype
    is_raw = 'r' in stype
    is_format = 'f' in stype
    content = m.group(3)
    if is_raw and (not is_format or not self.decode_escapes):
        string = self.norm_nl(content)
    elif is_raw and is_format:
        string = self.norm_nl(FE_RFESC.sub(self.replace_unicode, content))
    elif is_bytes:
        string = self.norm_nl(RE_BESC.sub(self.replace_bytes, content))
    elif is_format:
        string = self.norm_nl(RE_FESC.sub(self.replace_unicode, content))
    else:
        string = self.norm_nl(RE_ESC.sub(self.replace_unicode, content))
    return textwrap.dedent(RE_NON_PRINTABLE.sub('\n', string) if is_bytes else
        string), is_bytes
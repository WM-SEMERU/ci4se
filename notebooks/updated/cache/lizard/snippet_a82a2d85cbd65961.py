def from_text(text, origin=None, rdclass=dns.rdataclass.IN, relativize=True,
    zone_factory=Zone, filename=None, allow_include=False, check_origin=True):
    if filename is None:
        filename = '<string>'
    tok = dns.tokenizer.Tokenizer(text, filename)
    reader = _MasterReader(tok, origin, rdclass, relativize, zone_factory,
        allow_include=allow_include, check_origin=check_origin)
    reader.read()
    return reader.zone
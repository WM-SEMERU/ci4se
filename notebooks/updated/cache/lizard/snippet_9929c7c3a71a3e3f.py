def present(self, name, *args):
    if isinstance(name, (str, unicode)):
        name = dns.name.from_text(name, None)
    if len(args) == 0:
        rrset = self.find_rrset(self.answer, name, dns.rdataclass.ANY, dns.
            rdatatype.ANY, dns.rdatatype.NONE, None, True, True)
    elif isinstance(args[0], dns.rdataset.Rdataset) or isinstance(args[0],
        dns.rdata.Rdata) or len(args) > 1:
        if not isinstance(args[0], dns.rdataset.Rdataset):
            args = list(args)
            args.insert(0, 0)
        self._add(False, self.answer, name, *args)
    else:
        rdtype = args[0]
        if isinstance(rdtype, (str, unicode)):
            rdtype = dns.rdatatype.from_text(rdtype)
        rrset = self.find_rrset(self.answer, name, dns.rdataclass.ANY,
            rdtype, dns.rdatatype.NONE, None, True, True)
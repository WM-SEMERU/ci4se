def _split_capakey(self):
    import re
    match = re.match(
        '^[0-9]{5}[A-Z]{1}([0-9]{4})\\/([0-9]{2})([A-Z\\_]{1})([0-9]{3})$',
        self.capakey)
    if match:
        self.grondnummer = match.group(1)
        self.bisnummer = match.group(2)
        self.exponent = match.group(3)
        self.macht = match.group(4)
    else:
        raise ValueError("Invalid Capakey %s can't be parsed" % self.capakey)
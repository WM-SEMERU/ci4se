def format(self, tokensource, outfile):
    if self.encoding:
        outfile = codecs.lookup(self.encoding)[3](outfile)
    return self.format_unencoded(tokensource, outfile)
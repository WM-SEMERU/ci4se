def yyparse(self, cfgfile, splitstring=0):
    re_grammar = self._read_file(cfgfile)
    mma = self._mpda(re_grammar, splitstring)
    return mma
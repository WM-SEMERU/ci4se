def report(self, reporter):
    for symbol in sorted(self.unk_symbols.keys()):
        err = '{} ({}) is not part of IPA'.format(symbol.char, symbol.name)
        if symbol.char in self.common_err:
            repl = self.common_err[symbol.char]
            err += ', suggested replacement is {}'.format(repl)
            if len(repl) == 1:
                err += ' ({})'.format(unicodedata.name(repl))
        reporter.add(self.unk_symbols[symbol], err)
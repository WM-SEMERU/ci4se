def _complete_sig(self, symbol, attribute):
    fncall = self.context.el_name
    iexec, execmod = self.context.parser.tree_find(fncall, self.context.
        module, 'executables')
    if iexec is None:
        iexec, execmod = self.context.parser.tree_find(fncall, self.context
            .module, 'interfaces')
    if iexec is not None:
        if symbol == '':
            return iexec.parameters
        else:
            result = {}
            for ikey in iexec.parameters:
                if self._symbol_in(symbol, ikey):
                    result[ikey] = iexec.parameters[ikey]
            return result
    else:
        return self._complete_word(symbol, attribute)
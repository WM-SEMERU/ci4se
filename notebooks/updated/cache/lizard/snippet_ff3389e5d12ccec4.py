def import_handle(self, original, loc, tokens):
    if len(tokens) == 1:
        imp_from, imports = None, tokens[0]
    elif len(tokens) == 2:
        imp_from, imports = tokens
        if imp_from == '__future__':
            self.strict_err_or_warn(
                'unnecessary from __future__ import (Coconut does these automatically)'
                , original, loc)
            return ''
    else:
        raise CoconutInternalException('invalid import tokens', tokens)
    if self.strict:
        self.unused_imports.update(imported_names(imports))
    return universal_import(imports, imp_from=imp_from, target=self.target)
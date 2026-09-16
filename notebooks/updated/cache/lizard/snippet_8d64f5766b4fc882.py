def check_is_declared(self, id_, lineno, classname='identifier', scope=None,
    show_error=True):
    result = self.get_entry(id_, scope)
    if isinstance(result, symbols.TYPE):
        return True
    if result is None or not result.declared:
        if show_error:
            syntax_error(lineno, 'Undeclared %s "%s"' % (classname, id_))
        return False
    return True
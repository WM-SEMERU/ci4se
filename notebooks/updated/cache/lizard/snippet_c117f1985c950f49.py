def glob(self, pattern):
    pattern = self._flavour.casefold(pattern)
    drv, root, pattern_parts = self._flavour.parse_parts((pattern,))
    if drv or root:
        raise NotImplementedError('Non-relative patterns are unsupported')
    selector = _make_selector(tuple(pattern_parts))
    for p in selector.select_from(self):
        yield p
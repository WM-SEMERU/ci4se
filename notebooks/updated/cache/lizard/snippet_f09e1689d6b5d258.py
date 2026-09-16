def set_per_page(self, entries=100):
    if isinstance(entries, int) and entries <= 200:
        self.per_page = int(entries)
        return self
    else:
        raise SalesKingException('PERPAGE_ONLYINT',
            'Please set an integer <200 for the per-page limit')
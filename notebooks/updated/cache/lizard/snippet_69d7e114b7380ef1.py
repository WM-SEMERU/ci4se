def contains_no_backer(self, addr):
    for i, p in self._pages.items():
        if i * self._page_size <= addr < (i + 1) * self._page_size:
            return addr - i * self._page_size in p.keys()
    return False
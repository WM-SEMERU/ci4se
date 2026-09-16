def scan_until(self, regex):
    return self.search_full(regex, return_string=True, advance_pointer=True)
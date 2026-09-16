def superkey(self):
    sorted_list = []
    for header in self.header:
        if header in self._keys:
            sorted_list.append(header)
    return sorted_list
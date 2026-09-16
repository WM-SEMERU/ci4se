def search(self, name, value):
    partial = None
    header_name_search_result = CocaineHeaders.STATIC_TABLE_MAPPING.get(name)
    if header_name_search_result:
        index = header_name_search_result[1].get(value)
        if index is not None:
            return index, name, value
        partial = header_name_search_result[0], name, None
    offset = len(CocaineHeaders.STATIC_TABLE)
    for i, (n, v) in enumerate(self.dynamic_entries):
        if n == name:
            if v == value:
                return i + offset + 1, n, v
            elif partial is None:
                partial = i + offset + 1, n, None
    return partial
def add_extra_headers(self, sample_names):
    if not sample_names:
        return []
    full_headers = list(self.orient_data[sample_names[0]].keys())
    add_ons = []
    for head in full_headers:
        if head not in self.header_names:
            add_ons.append((head, head))
    return add_ons
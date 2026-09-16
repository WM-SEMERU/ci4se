def get_matching_indexes(self, idx_spec):
    if idx_spec is None or idx_spec == '':
        idx, hdu = self.find_first_good_hdu()
        return [idx]
    match = re.match('^\\[(.+)\\]$', idx_spec)
    if not match:
        return []
    idx_spec = match.group(1).strip()
    if ',' in idx_spec:
        name, extver = idx_spec.split(',')
        name, extver = name.strip(), extver.strip()
    else:
        name, extver = idx_spec.strip(), None
    name = name.upper()
    if extver is None:
        if re.match('^\\d+$', name):
            return [int(name)]
        extver = '1'
    idx_lst = []
    idx = 0
    for info in self.hdu_info:
        if name == '*' or name == info.name:
            if extver == '*' or extver == str(info.extver):
                idx_lst.append(info.index)
    return idx_lst
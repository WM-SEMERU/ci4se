def dissociate_values_or_ranges(self, vlan_id_range):
    values_or_ranges = vlan_id_range.split(',')
    vlan_ids = []
    if len(values_or_ranges) == 1 and '-' not in values_or_ranges[0]:
        vlan_ids = list(range(1, int(values_or_ranges[0]) + 1))
    else:
        for value_or_range in values_or_ranges:
            value_or_range.strip()
            if '-' not in value_or_range:
                vlan_ids.append(int(value_or_range))
            else:
                start, end = value_or_range.split('-')
                range_ids = range(int(start), int(end) + 1)
                vlan_ids.extend(range_ids)
    return vlan_ids
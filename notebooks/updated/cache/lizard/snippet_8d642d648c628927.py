def get_cycles(self):
    cycles = self.rater.find('cycles')
    if not cycles:
        return None
    starts = sorted([float(mrkr.text) for mrkr in cycles.findall('cyc_start')])
    ends = sorted([float(mrkr.text) for mrkr in cycles.findall('cyc_end')])
    cyc_list = []
    if not starts or not ends:
        return None
    if all(i < starts[0] for i in ends):
        raise ValueError('First cycle has no start.')
    for this_start, next_start in zip(starts, starts[1:] + [inf]):
        end_between_starts = [end for end in ends if this_start < end <=
            next_start]
        if len(end_between_starts) > 1:
            raise ValueError('Found more than one cycle end for same cycle')
        if end_between_starts:
            one_cycle = this_start, end_between_starts[0]
        else:
            one_cycle = this_start, next_start
        if one_cycle[1] == inf:
            raise ValueError('Last cycle has no end.')
        cyc_list.append(one_cycle)
    output = []
    for i, j in enumerate(cyc_list):
        cyc = j[0], j[1], i + 1
        output.append(cyc)
    return output
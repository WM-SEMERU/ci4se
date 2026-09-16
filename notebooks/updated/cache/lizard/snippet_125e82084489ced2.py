def get_max_sinkhole(self, length):
    ordered_sinks = sorted(list(self.sinkholes), key=operator.itemgetter(0),
        reverse=True)
    max_pair = None
    for addr, sz in ordered_sinks:
        if sz >= length:
            max_pair = addr, sz
            break
    if max_pair is None:
        return None
    remaining = max_pair[1] - length
    max_addr = max_pair[0] + remaining
    max_length = remaining
    self.sinkholes.remove(max_pair)
    if remaining:
        self.sinkholes.add((max_pair[0], max_length))
    return max_addr
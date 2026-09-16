def good_port_ranges(ports=None, min_range_len=20, border=3):
    min_range_len += border * 2
    if ports is None:
        ports = available_ports()
    ranges = utils.to_ranges(list(ports))
    lenghts = sorted([(r[1] - r[0], r) for r in ranges], reverse=True)
    long_ranges = [l[1] for l in lenghts if l[0] >= min_range_len]
    without_borders = [(low + border, high - border) for low, high in
        long_ranges]
    return without_borders
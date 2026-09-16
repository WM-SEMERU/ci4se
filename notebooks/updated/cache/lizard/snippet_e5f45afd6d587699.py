def parse_ports(ports_text):
    ports_set = set()
    for bit in ports_text.split(','):
        if '-' in bit:
            low, high = bit.split('-', 1)
            ports_set = ports_set.union(range(int(low), int(high) + 1))
        else:
            ports_set.add(int(bit))
    return sorted(list(ports_set))
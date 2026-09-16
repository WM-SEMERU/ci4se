def parse_chains(data):
    chains = odict()
    for line in data.splitlines(True):
        m = re_chain.match(line)
        if m:
            policy = None
            if m.group(2) != '-':
                policy = m.group(2)
            chains[m.group(1)] = {'policy': policy, 'packets': int(m.group(
                3)), 'bytes': int(m.group(4))}
    return chains
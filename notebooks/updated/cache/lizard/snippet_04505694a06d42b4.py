def parse_rules(data, chain):
    rules = []
    for line in data.splitlines(True):
        m = re_rule.match(line)
        if m and m.group(3) == chain:
            rule = parse_rule(m.group(4))
            rule.packets = int(m.group(1))
            rule.bytes = int(m.group(2))
            rules.append(rule)
    return rules
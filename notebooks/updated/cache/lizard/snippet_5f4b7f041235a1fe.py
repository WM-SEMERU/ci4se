def get_broadcast_events(cls, script):
    events = Counter()
    for name, _, block in cls.iter_blocks(script):
        if 'broadcast %s' in name:
            if isinstance(block.args[0], kurt.Block):
                events[True] += 1
            else:
                events[block.args[0].lower()] += 1
    return events
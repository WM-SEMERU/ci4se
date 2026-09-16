def _agent_from_distribution(distribution, value=-1, agent_id=None):
    if value < 0:
        value = random.random()
    for d in sorted(distribution, key=lambda x: x['threshold']):
        threshold = d['threshold']
        if not (agent_id is not None and threshold == STATIC_THRESHOLD and 
            agent_id in d['ids'] or value >= threshold[0] and value <
            threshold[1]):
            continue
        state = {}
        if 'state' in d:
            state = deepcopy(d['state'])
        return d['agent_type'], state
    raise Exception('Distribution for value {} not found in: {}'.format(
        value, distribution))